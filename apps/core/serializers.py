from collections import OrderedDict
from collections.abc import Mapping
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError
from rest_framework.settings import api_settings
from rest_framework.fields import SkipField
from rest_framework.fields import set_value
from rest_framework import serializers

from .mixins import IncludeCompanyMixin


class BaseSerializer(serializers.ModelSerializer, IncludeCompanyMixin):
    def create(self, validated_data):
        self.include(validated_data, self.context['request'])
        return super(BaseSerializer, self).create(validated_data)
        
    def to_internal_value(self, data):
        """
        Dict of native values <- Dict of primitive datatypes.
        """
        if not isinstance(data, Mapping):
            message = self.error_messages['invalid'].format(
                datatype=type(data).__name__
            )
            raise ValidationError({
                api_settings.NON_FIELD_ERRORS_KEY: [message]
            }, code='invalid')

        ret = OrderedDict()
        errors = OrderedDict()
        fields = self._writable_fields

        for field in fields:
            if field.field_name == 'company':
                continue

            validate_method = getattr(
                self, 'validate_' + field.field_name, None)
            primitive_value = field.get_value(data)
            try:
                validated_value = field.run_validation(primitive_value)
                if validate_method is not None:
                    validated_value = validate_method(validated_value)
            except ValidationError as exc:
                errors[field.field_name] = exc.detail
            except DjangoValidationError as exc:
                errors[field.field_name] = get_error_detail(exc)
            except SkipField:
                pass
            else:
                set_value(ret, field.source_attrs, validated_value)

        if errors:
            raise ValidationError(errors)

        return ret
