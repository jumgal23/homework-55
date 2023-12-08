def article_validate(description, detailed_description, created_at):
        errors = {}
        if not description:
            errors['description'] = 'Поле обязательное'
        elif len(description) > 200:
            errors['description'] = 'Максимальная длина 50 символов'

        if not detailed_description:
            errors['detailed_description'] = 'Поле обязательное'
        elif len(detailed_description) > 3000:
            errors['detailed_description'] = 'Максимальная длина 3000 символов'

        if not created_at:
            errors['created_at'] = 'Поле обязательное'
        elif len(created_at) > 40:
            errors['created_at'] = 'Максимальная длина 40 символов'

        return errors