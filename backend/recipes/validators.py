from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize > 10485760:
        raise ValidationError(
            "Вы не можете загрузить файл размером больше 1Mб")
    else:
        return value
