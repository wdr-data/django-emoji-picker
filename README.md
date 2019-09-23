# django-emoji-picker
Django app providing text input and textarea widgets with emoji picker.
It's based on [emoji-mart](https://github.com/missive/emoji-mart).

## Screenshot
![Screenshot](https://user-images.githubusercontent.com/3945220/40110572-9c6be100-5900-11e8-85a1-63bf21a9a646.png)

## Usage
This package contains a Django app that provides two widgets:

- `EmojiPickerTextInput`
- `EmojiPickerTextarea`

### Example

#### Installation
```bash
$ pip install django-emoji-picker
```

or

```bash
$ pipenv install django-emoji-picker
```

#### `settings.py`
```python
INSTALLED_APPS = [
    ...,
    'emoji_picker',
]
```

#### `<app>/admin/<model>.py` (for use with Django Admin)
```python
from emoji_picker.widgets import EmojiPickerTextInputAdmin, EmojiPickerTextareaAdmin


class YourModelForm(forms.ModelForm):
    short_text = forms.CharField(widget=EmojiPickerTextInputAdmin)
    long_text = forms.CharField(widget=EmojiPickerTextareaAdmin)
```

### Building from source
```bash
$ yarn
$ yarn build
```
