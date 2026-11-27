(() => {
  'use strict';
  const filter = document.querySelector('.rc-filter');
  const search = document.getElementById('rc-search');
  const select = document.getElementById('rc-grade');
  const count = document.getElementById('rc-count');
  const empty = document.getElementById('rc-empty');

  const normalize = value => value.toLowerCase().normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[’'.]/g, '')
    .replace(/[^a-z0-9]+/g, ' ').trim();

  const entries = [...document.querySelectorAll('.rc-section')].map(section => ({
    section,
    cards: [...section.querySelectorAll('.rc-card')].map(card => {
      const title = normalize(card.querySelector('h3').textContent);
      const author = normalize(card.querySelector('.rc-author').textContent);
      return {
        card,
        lo: Number(card.dataset.lo),
        hi: Number(card.dataset.hi),
        searchable: title + ' ' + author,
        compact: [title.replace(/ /g, ''), author.replace(/ /g, '')]
      };
    })
  }));

  function update() {
    const grade = Number(select.value);
    const query = normalize(search.value);
    const words = query.split(' ').filter(Boolean);
    const compactQuery = words.join('');
    let total = 0;
    for (const {section, cards} of entries) {
      let visible = 0;
      for (const {card, lo, hi, searchable, compact} of cards) {
        const gradeMatches = !grade || (grade >= lo && grade <= hi);
        const searchMatches = words.every(word => searchable.includes(word)) ||
          compact.some(entry => entry.includes(compactQuery));
        card.hidden = !gradeMatches || !searchMatches;
        if (!card.hidden) visible++;
      }
      section.hidden = visible === 0;
      total += visible;
    }
    const message = total + (total === 1 ? ' companion' : ' companions');
    if (count.textContent !== message) count.textContent = message;
    empty.hidden = total > 0;
  }

  search.addEventListener('input', update);
  select.addEventListener('change', update);
  window.addEventListener('pageshow', update);
  filter.hidden = false;
  update();
})();
