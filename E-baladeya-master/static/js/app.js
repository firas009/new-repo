document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-reveal]').forEach((element, index) => {
    element.style.animationDelay = `${index * 80}ms`;
    element.classList.add('reveal-in');
  });

  const searchInput = document.querySelector('#service-search');
  const filterButtons = document.querySelectorAll('[data-filter]');
  const serviceCards = document.querySelectorAll('[data-service-card]');
  const groups = document.querySelectorAll('[data-group]');
  const resultCount = document.querySelector('#service-count');
  const emptyResults = document.querySelector('#empty-results');
  let activeFilter = 'all';

  if (searchInput && serviceCards.length) {
    const updateCatalogue = () => {
      const query = searchInput.value.trim().toLowerCase();
      let visibleCount = 0;

      serviceCards.forEach((card) => {
        const group = card.closest('[data-group]');
        const matchesFilter = activeFilter === 'all' || group?.dataset.group === activeFilter;
        const matchesSearch = !query || card.dataset.search.includes(query);
        const visible = matchesFilter && matchesSearch;
        card.closest('.col-md-6').hidden = !visible;
        if (visible) visibleCount += 1;
      });

      groups.forEach((group) => {
        group.hidden = !group.querySelector('.col-md-6:not([hidden])');
      });
      resultCount.textContent = visibleCount;
      emptyResults.hidden = visibleCount !== 0;
    };

    searchInput.addEventListener('input', updateCatalogue);
    filterButtons.forEach((button) => {
      button.addEventListener('click', () => {
        activeFilter = button.dataset.filter;
        filterButtons.forEach((item) => item.classList.toggle('active', item === button));
        updateCatalogue();
      });
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === '/' && document.activeElement !== searchInput) {
        event.preventDefault();
        searchInput.focus();
      }
    });
  }
});
