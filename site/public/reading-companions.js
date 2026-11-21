(() => {
  'use strict';
  const filter = document.querySelector('.rc-filter');
  const select = document.getElementById('rc-grade');
  const sections = [...document.querySelectorAll('.rc-section')];
  const entries = sections.map(section => ({
    section,
    cards: [...section.querySelectorAll('.rc-card')]
  }));
  function update() {
    const grade = Number(select.value);
    let total = 0;
    for (const {section, cards} of entries) {
      let count = 0;
      for (const card of cards) {
        card.hidden = Boolean(grade && (grade < Number(card.dataset.lo) || grade > Number(card.dataset.hi)));
        if (!card.hidden) count++;
      }
      section.hidden = count === 0;
      total += count;
    }
    document.getElementById('rc-count').textContent = total + (total === 1 ? ' companion' : ' companions');
    document.getElementById('rc-empty').hidden = total > 0;
  }
  select.addEventListener('change', update);
  window.addEventListener('pageshow', update);
  filter.hidden = false;
  update();
})();
