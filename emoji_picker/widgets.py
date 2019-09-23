from django.forms.widgets import TextInput, Textarea
from django.contrib.admin.widgets import AdminTextInputWidget, AdminTextareaWidget

class MediaClass:
    js = (
        'emoji_picker/emoji-picker.js',
    )
    css = {
        'screen': (
            'emoji_picker/emoji-picker-panel.css',
            'emoji_picker/emoji-picker-main.css',
        )
    }

class EmojiPickerTextInput(TextInput):
    Media = MediaClass
    template_name = "emoji_picker/textinput.html"


class EmojiPickerTextInputAdmin(AdminTextInputWidget):
    Media = MediaClass
    template_name = "emoji_picker/textinput.html"


class EmojiPickerTextarea(Textarea):
    Media = MediaClass
    template_name = "emoji_picker/textarea.html"


class EmojiPickerTextareaAdmin(AdminTextareaWidget):
    Media = MediaClass
    template_name = "emoji_picker/textarea.html"
