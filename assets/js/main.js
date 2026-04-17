/**
 * ET-SL Elektrotechnik Schöcklland — Custom JS
 * No Bootstrap required
 */
(function () {
  'use strict';

  /* ----------------------------------------------------------------
     Header scroll effect
     ---------------------------------------------------------------- */
  function handleHeaderScroll() {
    const header = document.getElementById('header');
    if (!header) return;
    if (window.scrollY > 60) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }

  document.addEventListener('scroll', handleHeaderScroll, { passive: true });
  window.addEventListener('load', handleHeaderScroll);

  /* ----------------------------------------------------------------
     Mobile navigation
     ---------------------------------------------------------------- */
  const mobileToggle = document.getElementById('mobile-nav-toggle');
  const mobileClose = document.getElementById('mobile-nav-close');
  const mainNav = document.getElementById('main-nav');

  function openMobileNav() {
    if (!mainNav) return;
    mainNav.classList.add('open');
    if (mobileToggle) mobileToggle.style.display = 'none';
    if (mobileClose) mobileClose.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }

  function closeMobileNav() {
    if (!mainNav) return;
    mainNav.classList.remove('open');
    if (mobileToggle) mobileToggle.style.display = '';
    if (mobileClose) mobileClose.style.display = 'none';
    document.body.style.overflow = '';
    // Close any open dropdowns
    document.querySelectorAll('#main-nav .dropdown.open').forEach(function (d) {
      d.classList.remove('open');
    });
  }

  if (mobileToggle) {
    mobileToggle.addEventListener('click', function () {
      if (mainNav && mainNav.classList.contains('open')) {
        closeMobileNav();
      } else {
        openMobileNav();
      }
    });
  }

  // Close button
  if (mobileClose) {
    mobileClose.addEventListener('click', closeMobileNav);
  }

  // Close when clicking backdrop (the semi-transparent overlay behind the panel)
  if (mainNav) {
    mainNav.addEventListener('click', function (e) {
      if (e.target === mainNav) {
        closeMobileNav();
      }
    });
  }

  // Close on nav link click (but NOT dropdown parent links)
  document.querySelectorAll('#main-nav .nav-links a').forEach(function (link) {
    // Skip the dropdown parent link — that should toggle the submenu, not close nav
    if (link.parentElement && link.parentElement.classList.contains('dropdown')) return;
    link.addEventListener('click', closeMobileNav);
  });

  // Also close on dropdown sub-link click
  document.querySelectorAll('#main-nav .dropdown-menu a').forEach(function (link) {
    link.addEventListener('click', closeMobileNav);
  });

  /* ----------------------------------------------------------------
     Mobile dropdown toggle (no hover on touch devices)
     ---------------------------------------------------------------- */
  document.querySelectorAll('#main-nav .dropdown > a').forEach(function (link) {
    link.addEventListener('click', function (e) {
      // Only intercept on mobile (when the mobile nav panel is open)
      if (!mainNav || !mainNav.classList.contains('open')) return;
      e.preventDefault();
      var parent = this.parentElement;
      var wasOpen = parent.classList.contains('open');
      // Close all other dropdowns
      document.querySelectorAll('#main-nav .dropdown.open').forEach(function (d) {
        d.classList.remove('open');
      });
      // Toggle this one
      if (!wasOpen) {
        parent.classList.add('open');
      }
    });
  });

  /* ----------------------------------------------------------------
     Scroll to top button
     ---------------------------------------------------------------- */
  const scrollTopBtn = document.getElementById('scroll-top');

  function toggleScrollTop() {
    if (!scrollTopBtn) return;
    if (window.scrollY > 300) {
      scrollTopBtn.classList.add('active');
    } else {
      scrollTopBtn.classList.remove('active');
    }
  }

  if (scrollTopBtn) {
    scrollTopBtn.addEventListener('click', function (e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  document.addEventListener('scroll', toggleScrollTop, { passive: true });
  window.addEventListener('load', toggleScrollTop);

  /* ----------------------------------------------------------------
     FAQ Accordion
     ---------------------------------------------------------------- */
  document.querySelectorAll('.faq-question').forEach(function (btn) {
    btn.addEventListener('click', function () {
      const item = this.closest('.faq-item');
      const isActive = item.classList.contains('active');

      // Close all
      document.querySelectorAll('.faq-item.active').forEach(function (openItem) {
        openItem.classList.remove('active');
      });

      // Open clicked (if it wasn't already open)
      if (!isActive) {
        item.classList.add('active');
      }
    });
  });

  /* ----------------------------------------------------------------
     Preloader
     ---------------------------------------------------------------- */
  const preloader = document.getElementById('preloader');
  if (preloader) {
    window.addEventListener('load', function () {
      preloader.style.opacity = '0';
      preloader.style.visibility = 'hidden';
      setTimeout(function () {
        preloader.remove();
      }, 400);
    });
  }

  /* ----------------------------------------------------------------
     AOS Init
     ---------------------------------------------------------------- */
  window.addEventListener('load', function () {
    if (typeof AOS !== 'undefined') {
      AOS.init({
        duration: 600,
        easing: 'ease-in-out',
        once: true,
        mirror: false,
      });
    }
  });

  /* ----------------------------------------------------------------
     GLightbox Init
     ---------------------------------------------------------------- */
  if (typeof GLightbox !== 'undefined') {
    GLightbox({ selector: '.glightbox' });
  }

  /* ----------------------------------------------------------------
     Smooth scroll for anchor links
     ---------------------------------------------------------------- */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#' || targetId === '#top') return; // scroll-top handled separately
      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        const headerH = document.getElementById('header');
        const offset = headerH ? headerH.offsetHeight + 16 : 80;
        const top = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top: top, behavior: 'smooth' });
      }
    });
  });

  /* ----------------------------------------------------------------
     Scrollspy — active nav link
     ---------------------------------------------------------------- */
  const navLinks = document.querySelectorAll('.nav-links a');

  function updateScrollspy() {
    const scrollPos = window.scrollY + 200;

    navLinks.forEach(function (link) {
      const href = link.getAttribute('href');
      if (!href) return;
      // Handle both "#section" and "index.html#section"
      const hashIndex = href.indexOf('#');
      if (hashIndex === -1) return;
      const hash = href.substring(hashIndex);
      if (!hash || hash === '#') return;

      const section = document.querySelector(hash);
      if (!section) return;

      if (scrollPos >= section.offsetTop && scrollPos < section.offsetTop + section.offsetHeight) {
        navLinks.forEach(function (l) { l.classList.remove('active'); });
        link.classList.add('active');
      }
    });
  }

  document.addEventListener('scroll', updateScrollspy, { passive: true });
  window.addEventListener('load', updateScrollspy);

  /* ----------------------------------------------------------------
     Hash link scroll correction on page load
     ---------------------------------------------------------------- */
  window.addEventListener('load', function () {
    if (window.location.hash) {
      const target = document.querySelector(window.location.hash);
      if (target) {
        setTimeout(function () {
          const header = document.getElementById('header');
          const offset = header ? header.offsetHeight + 16 : 80;
          window.scrollTo({
            top: target.offsetTop - offset,
            behavior: 'smooth',
          });
        }, 100);
      }
    }
  });

})();