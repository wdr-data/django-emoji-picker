from django.forms.widgets import TextInput, Textarea


class EmojiPickerTextInput(TextInput):
    class Media:
        js = (
            'emoji_picker/emoji-picker.js',
        )
        css = {
            'screen': (
                'emoji_picker/emoji-picker-panel.css',
                'emoji_picker/emoji-picker-main.css',
            )
        }

    template_name = "emoji_picker/textinput.html"


class EmojiPickerTextarea(Textarea):
    class Media:
        js = (
            'emoji_picker/emoji-picker.js',
        )
        css = {
            'screen': (
                'emoji_picker/emoji-picker-panel.css',
                'emoji_picker/emoji-picker-main.css',
            )
        }

    template_name = "emoji_picker/textarea.html"
