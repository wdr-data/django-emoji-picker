import React from 'react';
import { render } from 'react-dom';
import { Picker } from 'emoji-mart';

document.addEventListener('DOMContentLoaded', () => {
  let panelOpen = false;
  let currentField;
  let currentButton;

  const picker = React.createElement(Picker, {
    set: 'emojione',
    autofocus: true,
    onSelect: (emoji) => {
      if (!currentField) return;

      const from = currentField.selectionStart;
      const to = currentField.selectionEnd;

      currentField.value = currentField.value.substring(0, from) + emoji.native + currentField.value.substring(to)
    },
    onClick: (emoji, event) => currentButton.focus(),
  });

  const panel = document.createElement('div');
  panel.classList.add('dep-panel');

  render(picker, panel);
  document.body.appendChild(panel);

  const isInTarget = (elem, target) => elem === target || elem.contains(target);

  const clickHandler = (e) => {
    if (!panelOpen || isInTarget(currentButton, e.target) || isInTarget(panel, e.target)) return;
    panel.style.display = 'none';
    panelOpen = false;
  };

  document.body.addEventListener('click', clickHandler, true);

  document.querySelectorAll('.dep-button').forEach(
    (elem) => {
      elem.addEventListener('click', (e) => {
        const {left, bottom} = e.target.getBoundingClientRect();
        panel.style.top = `${window.scrollY + bottom + 5}px`;
        panel.style.left = `${window.scrollX + left}px`;
        panel.style.display = 'block';

        setTimeout(() => panelOpen = true);
        currentField = e.currentTarget.parentNode.firstElementChild;
        currentButton = e.currentTarget;
      });
    }
  );
});
