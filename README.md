# django-emoji-picker
Django app providing text input and textarea widgets with emoji picker.
It's based on [emoji-mart](https://github.com/missive/emoji-mart).

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
from emoji_picker.widgets import EmojiPickerTextInput, EmojiPickerTextarea


class YourModelForm(forms.ModelForm):
    short_text = forms.CharField(widget=EmojiPickerTextInput)
    long_text = forms.CharField(widget=EmojiPickerTextarea)
```

### Building from source
```bash
$ yarn
$ yarn build
```
