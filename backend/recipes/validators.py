from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize > 1048576:
        raise ValidationError(
            "Вы не можете загрузить файл размером больше 1Mб")
    else:
        return value
