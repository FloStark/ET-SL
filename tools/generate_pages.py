import os

# This script matches the SEO and Accessibility improvements 
# (Local Fonts, Skip-Links, Breadcrumbs, JSON-LD, Internal Linking).

template_top = """<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <title>{TITLE} | Elektrotechnik Schöcklland ET-SL GmbH</title>
  <meta name="description" content="{DESC}">
  <meta name="keywords" content="{KEYWORDS}">

  <meta name="google-site-verification" content="0B6TFXYVNonPg6ZPElsI6da4UFmIbH6pGzhy94DIIcs" />

  <!-- Canonical URL -->
  <link rel="canonical" href="https://et-sl.at/{FILENAME}">

  <!-- Open Graph / Social Media -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://et-sl.at/{FILENAME}">
  <meta property="og:title" content="{TITLE} | Elektrotechnik Schöcklland">
  <meta property="og:description" content="{DESC}">
  <meta property="og:image" content="https://et-sl.at/assets/img/Logo_final.svg">
  <meta property="og:locale" content="de_AT">

  <link href="assets/img/favicon.ico" rel="icon">
  <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="assets/vendor/aos/aos.css" rel="stylesheet">
  <link href="assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
  <link href="assets/css/main.css" rel="stylesheet">

  <!-- JSON-LD Structured Data for Service/Page -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "WebPage",
        "name": "{TITLE}",
        "publisher": {{
          "@type": "Electrician",
          "name": "Elektrotechnik Schöcklland - ET-SL GmbH",
          "logo": "https://et-sl.at/assets/img/Logo_final.svg"
        }}
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "Startseite",
            "item": "https://et-sl.at/"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "{BREADCRUMB}",
            "item": "https://et-sl.at/{{FILENAME}}"
          }}
        ]
      }}
    ]
  }}
  </script>
</head>
<body>
  <a href="#main-content" class="skip-link">Zum Inhalt springen</a>
  <!-- ==================== Header ==================== -->
  <header class="site-header" id="header">
    <div class="container">
      <a href="index.html" class="logo">
        <img src="assets/img/logo.png" alt="Elektrotechnik Schöcklland ET-SL GmbH Logo">
      </a>

      <nav class="main-nav" id="main-nav">
        <ul class="nav-links">
          <li><a href="index.html">Start</a></li>
          <li class="dropdown">
            <a href="index.html#leistungen">Leistungen</a>
            <div class="dropdown-menu">
              <a href="photovoltaik.html">Photovoltaik &amp; Speicher</a>
              <a href="elektroinstallation.html">Elektroinstallation &amp; Smart Home</a>
              <a href="e-mobilitaet.html">E-Mobilität</a>
            </div>
          </li>
          <li><a href="ueber-uns.html">Über uns</a></li>
          <li><a href="karriere.html">Karriere</a></li>
          <li><a href="index.html#contact">Kontakt</a></li>
        </ul>
      </nav>

      <a class="btn btn-primary header-cta" href="index.html#contact">Kontaktiere uns</a>

      <button class="mobile-nav-toggle" id="mobile-nav-toggle" aria-label="Menü öffnen">
        <i class="bi bi-list"></i>
      </button>

      <button class="mobile-nav-close" id="mobile-nav-close" aria-label="Menü schließen">
        <i class="bi bi-x-lg"></i>
      </button>
    </div>
  </header>
  <!-- Visual Breadcrumbs -->
  <nav class="breadcrumb-nav" aria-label="Breadcrumb">
    <div class="container">
      <div class="breadcrumb">
        <a href="index.html">Startseite</a>
        <span class="separator"><i class="bi bi-chevron-right"></i></span>
        <span class="current">{BREADCRUMB}</span>
      </div>
    </div>
  </nav>

  <!-- ==================== Main Content ==================== -->
  <main id="main-content">
"""

template_bottom = """
  </main>
  <footer class="site-footer" id="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-about">
          <a href="index.html" class="footer-brand">ET-SL GmbH</a>
          <div class="footer-contact-info">
            <p>Grazer Straße 63</p>
            <p>8061 St. Radegund bei Graz</p>
            <p style="margin-top: 12px;"><strong>Telefon:</strong> <a href="tel:+436644120512">0664 4120512</a></p>
            <p><strong>Email:</strong> <a href="mailto:office@et-sl.at">office@et-sl.at</a></p>
          </div>
        </div>
        <div class="footer-links">
          <h4>Wissenswertes</h4>
          <ul>
            <li><i class="bi bi-chevron-right"></i> <a href="impressum.html">Impressum</a></li>
            <li><i class="bi bi-chevron-right"></i> <a href="datenschutz.html">Datenschutzerklärung</a></li>
            <li><i class="bi bi-chevron-right"></i> <a href="agb.html">AGB</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2026 <strong>ET-SL GmbH</strong> – Alle Rechte vorbehalten.</p>
        <div class="murix-credits">
          Made by <a href="https://murix.at" target="_blank">Murix.at</a>
        </div>
      </div>
    </div>
  </footer>
  <a href="#" id="scroll-top" class="scroll-top" aria-label="Nach oben scrollen">
    <i class="bi bi-arrow-up-short"></i>
  </a>
  <div id="preloader"></div>
  <script src="assets/vendor/aos/aos.js"></script>
  <script src="assets/vendor/glightbox/js/glightbox.min.js"></script>
  <script src="assets/js/main.js"></script>
  <!-- Cookie Consent Banner -->
  <div id="cookie-consent" class="cookie-consent">
    <div class="cookie-consent-inner">
      <div class="cookie-consent-text">
        <strong>Cookie-Hinweis</strong><br>
        Diese Website verwendet Cookies und lädt externe Dienste (Google Maps) für die bestmögliche Nutzererfahrung.
        Mehr dazu in unserer <a href="datenschutz.html">Datenschutzerklärung</a>.
      </div>
      <div class="cookie-consent-actions">
        <button onclick="acceptCookies()" class="cookie-btn cookie-btn-accept">Akzeptieren</button>
        <button onclick="declineCookies()" class="cookie-btn cookie-btn-decline">Nur notwendige</button>
      </div>
    </div>
  </div>
  <script>
    function acceptCookies() {
      localStorage.setItem('cookie-consent', 'accepted');
      document.getElementById('cookie-consent').style.display = 'none';
    }
    function declineCookies() {
      localStorage.setItem('cookie-consent', 'declined');
      document.getElementById('cookie-consent').style.display = 'none';
      var maps = document.querySelectorAll('iframe[src*="google.com/maps"]');
      maps.forEach(function (m) {
        var notice = document.createElement('div');
        notice.className = 'map-disabled';
        notice.innerHTML = '<i class="bi bi-geo-alt"></i> Karte deaktiviert. <a href="https://maps.google.com/?q=Grazer+Stra%C3%9Fe+63+8061+St.+Radegund" target="_blank" rel="noopener">In Google Maps öffnen</a>';
        m.parentNode.replaceChild(notice, m);
      });
    }
    if (!localStorage.getItem('cookie-consent')) {
      document.getElementById('cookie-consent').style.display = 'block';
    } else if (localStorage.getItem('cookie-consent') === 'declined') {
      declineCookies();
    }
  </script>
</body>
</html>
"""

pages = {
    "photovoltaik.html": {
        "title": "Photovoltaik & Stromspeicher in Graz Umgebung",
        "desc": "Ihr Experte für Photovoltaik, Solaranlagen und Stromspeicher in St. Radegund und Graz Umgebung. Jetzt Förderungen sichern.",
        "keywords": "Photovoltaik Graz, Solaranlage St. Radegund, Stromspeicher Steiermark, PV Installateur",
        "content": """
    <section class="section" style="padding-top: var(--space-4xl);">
      <div class="container">
        <div class="section-header" data-aos="fade-up">
          <span class="section-label">Erneuerbare Energien</span>
          <h1>Photovoltaik & Stromspeicher</h1>
        </div>
        <div style="max-width: 800px; margin: 0 auto; line-height: 1.8; color: var(--color-muted);" data-aos="fade-up" data-aos-delay="100">
          <p style="font-size: var(--font-size-lg); color: var(--color-heading); font-weight: 500; margin-bottom: var(--space-md);">Nutzen Sie die Kraft der Sonne!</p>
          <p>Mit einer maßgeschneiderten Photovoltaikanlage von ET-SL GmbH machen Sie sich unabhängig von steigenden Strompreisen und leisten einen aktiven Beitrag zum Umweltschutz. Wir begleiten Sie von der ersten Beratung über die Konzeption bis hin zur schlüsselfertigen Übergabe.</p>
          
          <h3 style="margin-top: var(--space-xl); margin-bottom: var(--space-md); color: var(--color-heading);">Unsere PV-Leistungen:</h3>
          <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 15px;">
            <li style="display: flex;"><i class="bi bi-lightning-charge-fill" style="color: var(--color-primary); margin-right: 15px; font-size: 20px;"></i><span><strong>Individuelle Planung:</strong> Berechnung von Ertrag, Eigenverbrauchsquote und Amortisation basierend auf Ihrem Stromverbrauch.</span></li>
            <li style="display: flex;"><i class="bi bi-lightning-charge-fill" style="color: var(--color-primary); margin-right: 15px; font-size: 20px;"></i><span><strong>Photovoltaik-Module:</strong> Fachgerechte Installation von leistungsstarken, langlebigen Solarmodulen auf dem Dach.</span></li>
            <li style="display: flex;"><i class="bi bi-lightning-charge-fill" style="color: var(--color-primary); margin-right: 15px; font-size: 20px;"></i><span><strong>Stromspeicher-Systeme:</strong> Zwischenspeicherung des Solarstroms für die Nutzung in der Nacht, für maximale Autarkie.</span></li>
            <li style="display: flex;"><i class="bi bi-lightning-charge-fill" style="color: var(--color-primary); margin-right: 15px; font-size: 20px;"></i><span><strong>Fördermanagement:</strong> Vollständige Unterstützung bei der Abwicklung der EAG-Förderungen und Landesförderungen Steiermark.</span></li>
          </ul>
          
          <div style="margin-top: var(--space-2xl); text-align: center;">
            <a href="index.html#contact" class="btn btn-primary btn-lg">Kostenlosen Beratungstermin vereinbaren</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt" style="background: var(--color-bg-alt); padding: var(--space-3xl) 0;">
      <div class="container">
        <div class="section-header" data-aos="fade-up">
          <h2>Weitere Leistungen</h2>
          <p>Entdecken Sie unser gesamtes Portfolio für Ihr Zuhause.</p>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: var(--space-lg);" data-aos="fade-up" data-aos-delay="100">
          <a href="elektroinstallation.html" class="service-card-mini" style="background: var(--color-white); padding: var(--space-xl); border-radius: var(--radius-lg); border: 1px solid var(--color-border); text-align: center; transition: all 0.3s ease;">
            <i class="bi bi-plug" style="font-size: 32px; color: var(--color-primary); margin-bottom: 15px; display: block;"></i>
            <h4 style="margin-bottom: 10px;">Elektroinstallation</h4>
            <p style="font-size: var(--font-size-sm); color: var(--color-muted);">Vom Neubau bis zur Sanierung – wir kümmern uns um Ihre Elektrik.</p>
          </a>
          <a href="e-mobilitaet.html" class="service-card-mini" style="background: var(--color-white); padding: var(--space-xl); border-radius: var(--radius-lg); border: 1px solid var(--color-border); text-align: center; transition: all 0.3s ease;">
            <i class="bi bi-ev-front" style="font-size: 32px; color: var(--color-primary); margin-bottom: 15px; display: block;"></i>
            <h4 style="margin-bottom: 10px;">E-Mobilität</h4>
            <p style="font-size: var(--font-size-sm); color: var(--color-muted);">Sicher und schnell zu Hause laden mit der passenden Wallbox.</p>
          </a>
        </div>
      </div>
    </section>
"""
    },
    "elektroinstallation.html": {
        "title": "Elektroinstallation & Smart Home vom Meisterbetrieb",
        "desc": "Professionelle Elektroinstallation, Haussteuerung und Smart Home Systeme (KNX) in St. Radegund und Graz Umgebung vom Meisterbetrieb ET-SL.",
        "keywords": "Elektroinstallation Graz, Elektriker St. Radegund, Smart Home KNX Steiermark, Hausverkabelung",
        "content": """
    <section class="section" style="padding-top: var(--space-4xl);">
      <div class="container">
        <div class="section-header" data-aos="fade-up">
          <span class="section-label">Gebäudetechnik</span>
          <h1>Elektroinstallation & Smart Home</h1>
        </div>
        <div style="max-width: 800px; margin: 0 auto; line-height: 1.8; color: var(--color-muted);" data-aos="fade-up" data-aos-delay="100">
          <p style="font-size: var(--font-size-lg); color: var(--color-heading); font-weight: 500; margin-bottom: var(--space-md);">Sicherheit und Komfort für Ihr Zuhause.</p>
          <p>Ob privater Neubau, umfangreiche Altbausanierung oder modernisiertes Gewerbeobjekt – wir bieten das gesamte Spektrum der modernen Elektrotechnik aus einer Hand. Präzision, Normkonformität und zukunftssichere Technologien stehen bei uns im Mittelpunkt.</p>
          
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: var(--space-lg); margin-top: var(--space-xl);">
            <div style="background: var(--color-bg-alt); padding: var(--space-lg); border-radius: var(--radius-md); border: 1px solid var(--color-border);">
              <h4 style="color: var(--color-heading); margin-bottom: 10px;">Klassische Hausinstallation</h4>
              <p style="font-size: var(--font-size-sm);">Komplette Leitungsverlegung, Steckdosen, Schalterprogramme und Beleuchtung für Neubau und Kernsanierung.</p>
            </div>
            <div style="background: var(--color-bg-alt); padding: var(--space-lg); border-radius: var(--radius-md); border: 1px solid var(--color-border);">
              <h4 style="color: var(--color-heading); margin-bottom: 10px;">Verteilerbau</h4>
              <p style="font-size: var(--font-size-sm);">Planung und fachgerechte Ausführung von aufgeräumten und sicheren Schaltschränken und Zählerverteilern nach ÖVE-Norm.</p>
            </div>
            <div style="background: var(--color-bg-alt); padding: var(--space-lg); border-radius: var(--radius-md); border: 1px solid var(--color-border);">
              <h4 style="color: var(--color-heading); margin-bottom: 10px;">Smart Home Systeme</h4>
              <p style="font-size: var(--font-size-sm);">Intelligente Steuerung von Beleuchtung, Heizung und Rollläden. Wir integrieren KNX- und Funksysteme für maximalen Wohnkomfort.</p>
            </div>
            <div style="background: var(--color-bg-alt); padding: var(--space-lg); border-radius: var(--radius-md); border: 1px solid var(--color-border);">
              <h4 style="color: var(--color-heading); margin-bottom: 10px;">Sicherheitstechnik</h4>
              <p style="font-size: var(--font-size-sm);">Schützen Sie Ihr Eigentum mit zuverlässigen Alarmanlagen und modernen Videoüberwachungssystemen.</p>
            </div>
          </div>
          
          <div style="margin-top: var(--space-2xl); text-align: center;">
            <a href="index.html#contact" class="btn btn-primary btn-lg">Jetzt Bauprojekt anfragen</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt" style="background: var(--color-bg-alt); padding: var(--space-3xl) 0;">
      <div class="container">
        <div class="section-header" data-aos="fade-up">
          <h2>Weitere Leistungen</h2>
          <p>Entdecken Sie unser gesamtes Portfolio für Ihr Zuhause.</p>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: var(--space-lg);" data-aos="fade-up" data-aos-delay="100">
          <a href="photovoltaik.html" class="service-card-mini" style="background: var(--color-white); padding: var(--space-xl); border-radius: var(--radius-lg); border: 1px solid var(--color-border); text-align: center; transition: all 0.3s ease;">
            <i class="bi bi-sun" style="font-size: 32px; color: var(--color-primary); margin-bottom: 15px; display: block;"></i>
            <h4 style="margin-bottom: 10px;">Photovoltaik</h4>
            <p style="font-size: var(--font-size-sm); color: var(--color-muted);">Maßgeschneiderte Solaranlagen und Stromspeicher für Ihre Unabhängigkeit.</p>
          </a>
          <a href="e-mobilitaet.html" class="service-card-mini" style="background: var(--color-white); padding: var(--space-xl); border-radius: var(--radius-lg); border: 1px solid var(--color-border); text-align: center; transition: all 0.3s ease;">
            <i class="bi bi-ev-front" style="font-size: 32px; color: var(--color-primary); margin-bottom: 15px; display: block;"></i>
            <h4 style="margin-bottom: 10px;">E-Mobilität</h4>
            <p style="font-size: var(--font-size-sm); color: var(--color-muted);">Sicher und schnell zu Hause laden mit der passenden Wallbox.</p>
          </a>
        </div>
      </div>
    </section>
"""
    },
    "e-mobilitaet.html": {
        "title": "E-Mobilität & Wallboxen in Graz Umgebung",
        "desc": "Sichere Ladestationen und Wallboxen für Ihr Elektroauto installieren lassen. ET-SL ist Ihr Partner für E-Mobilität in St. Radegund und Graz.",
        "keywords": "E-Mobilität Graz, Wallbox installieren St. Radegund, Ladestation Elektroauto Steiermark",
        "content": """
    <section class="section" style="padding-top: var(--space-4xl);">
      <div class="container">
        <div class="section-header" data-aos="fade-up">
          <span class="section-label">Zukunft der Fortbewegung</span>
          <h1>E-Mobilität & Ladeinfrastruktur</h1>
        </div>
        <div style="max-width: 800px; margin: 0 auto; line-height: 1.8; color: var(--color-muted);" data-aos="fade-up" data-aos-delay="100">
          <p style="font-size: var(--font-size-lg); color: var(--color-heading); font-weight: 500; margin-bottom: var(--space-md);">Sicher und schnell Zuhause laden.</p>
          <p>Die reine Haushaltssteckdose ist für Elektroautos ungeeignet. Wir installieren die passende Wandladestation (Wallbox), damit Sie Ihr E-Auto sicher und in kürzester Zeit aufladen können – idealerweise kombiniert mit eigenem Solarstrom.</p>
          
          <h3 style="margin-top: var(--space-xl); margin-bottom: var(--space-md); color: var(--color-heading);">Ladungslösungen von ET-SL:</h3>
          <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 10px;">
            <li><i class="bi bi-chevron-right" style="color: var(--color-primary); margin-right: 10px;"></i><strong>Heimische Wallboxen:</strong> Kompakte und leistungsstarke 11 kW oder 22 kW AC-Ladestationen für Garage und Carport.</li>
            <li><i class="bi bi-chevron-right" style="color: var(--color-primary); margin-right: 10px;"></i><strong>PV-Überschussladen:</strong> Kopplung der Wallbox mit Ihrer Photovoltaikanlage, sodass nur der gratis überschüssige Sonnenstrom getankt wird.</li>
            <li><i class="bi bi-chevron-right" style="color: var(--color-primary); margin-right: 10px;"></i><strong>Lastmanagement für Wohnanlagen:</strong> Damit beim gleichzeitigen Laden mehrerer E-Autos in Tiefgaragen der Netzanschluss nicht überlastet wird.</li>
            <li><i class="bi bi-chevron-right" style="color: var(--color-primary); margin-right: 10px;"></i><strong>Förderberatung:</strong> Unterstützung bei der Einreichung von staatlichen Förderzuschüssen für Ladeinfrastruktur in der Steiermark.</li>
          </ul>
          
          <div style="margin-top: var(--space-2xl); text-align: center;">
            <a href="index.html#contact" class="btn btn-primary btn-lg">Wallbox Angebot einholen</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt" style="background: var(--color-bg-alt); padding: var(--space-3xl) 0;">
      <div class="container">
        <div class="section-header" data-aos="fade-up">
          <h2>Weitere Leistungen</h2>
          <p>Entdecken Sie unser gesamtes Portfolio für Ihr Zuhause.</p>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: var(--space-lg);" data-aos="fade-up" data-aos-delay="100">
          <a href="photovoltaik.html" class="service-card-mini" style="background: var(--color-white); padding: var(--space-xl); border-radius: var(--radius-lg); border: 1px solid var(--color-border); text-align: center; transition: all 0.3s ease;">
            <i class="bi bi-sun" style="font-size: 32px; color: var(--color-primary); margin-bottom: 15px; display: block;"></i>
            <h4 style="margin-bottom: 10px;">Photovoltaik</h4>
            <p style="font-size: var(--font-size-sm); color: var(--color-muted);">Maßgeschneiderte Solaranlagen und Stromspeicher für Ihre Unabhängigkeit.</p>
          </a>
          <a href="elektroinstallation.html" class="service-card-mini" style="background: var(--color-white); padding: var(--space-xl); border-radius: var(--radius-lg); border: 1px solid var(--color-border); text-align: center; transition: all 0.3s ease;">
            <i class="bi bi-plug" style="font-size: 32px; color: var(--color-primary); margin-bottom: 15px; display: block;"></i>
            <h4 style="margin-bottom: 10px;">Elektroinstallation</h4>
            <p style="font-size: var(--font-size-sm); color: var(--color-muted);">Vom Neubau bis zur Sanierung – wir kümmern uns um Ihre Elektrik.</p>
          </a>
        </div>
      </div>
    </section>
"""
    },
    "karriere.html": {
        "title": "Karriere bei ET-SL - jobs",
        "desc": "Jobs in der Elektrotechnik Graz-Umgebung: Werden Sie Teil von ET-SL in St. Radegund. Wir suchen Elektrotechniker und Lehrlinge.",
        "keywords": "Karriere Elektriker Graz, Job Elektrotechnik Steiermark, Lehrstelle Elektrotechniker, ET-SL Jobs",
        "content": """
    <section class="section" style="padding-top: var(--space-4xl);">
      <div class="container">
        <div class="section-header" data-aos="fade-up">
          <span class="section-label">Werde Teil des Teams</span>
          <h1>Karriere bei ET-SL GmbH</h1>
        </div>
        <div style="max-width: 800px; margin: 0 auto; line-height: 1.8; color: var(--color-muted);" data-aos="fade-up" data-aos-delay="100">
          <p>Du hast eine Leidenschaft für Technik, arbeitest gerne präzise und suchst ein Umfeld, in dem deine Arbeit wertgeschätzt wird? Wir sind immer auf der Suche nach tatkräftiger Unterstützung für unser Team in St. Radegund.</p>
          
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-md); margin-top: var(--space-xl); margin-bottom: var(--space-2xl);">
            <div style="background: rgba(16, 188, 105, 0.05); padding: var(--space-lg); border-radius: var(--radius-md); border-left: 4px solid var(--color-primary);">
              <h4 style="color: var(--color-heading); margin-bottom: 5px;">Elektrotechniker/in</h4>
              <p style="font-size: var(--font-size-sm); margin: 0;">Geselle/in oder Meister/in für abwechslungsreiche Anlagenmontage.</p>
            </div>
            <div style="background: rgba(16, 188, 105, 0.05); padding: var(--space-lg); border-radius: var(--radius-md); border-left: 4px solid var(--color-primary);">
              <h4 style="color: var(--color-heading); margin-bottom: 5px;">Lehrlinge gesucht!</h4>
              <p style="font-size: var(--font-size-sm); margin: 0;">Ausbildung im zukunftssicheren Bereich der Elektrotechnik & erneuerbaren Energien.</p>
            </div>
          </div>
          
          <h3 style="margin-top: var(--space-xl); margin-bottom: var(--space-md); color: var(--color-heading);">Warum bei uns arbeiten?</h3>
          <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 10px;">
            <li><i class="bi bi-star-fill" style="color: #fbbf24; margin-right: 10px;"></i><strong>Top Equipment:</strong> Hochwertiges Werkzeug und moderne Firmenfahrzeuge.</li>
            <li><i class="bi bi-star-fill" style="color: #fbbf24; margin-right: 10px;"></i><strong>Zukunftsmärkte:</strong> Spannende Projekte mit Photovoltaik und Smart Home statt Fließbandarbeit.</li>
            <li><i class="bi bi-star-fill" style="color: #fbbf24; margin-right: 10px;"></i><strong>Regionalität:</strong> Keine wochenlangen Montagen. Feierabend zu Hause in der Region Graz.</li>
            <li><i class="bi bi-star-fill" style="color: #fbbf24; margin-right: 10px;"></i><strong>Wir-Gefühl:</strong> Ein familiäres Team mit flachen Hierarchien und echtem Zusammenhalt.</li>
          </ul>
          
          <!-- Initiativbewerbung -->
          <div style="margin-top: var(--space-3xl); background: var(--color-white); padding: var(--space-2xl); border-radius: var(--radius-lg); text-align: center; border: 1px solid var(--color-border); box-shadow: var(--shadow-md);">
            <h3 style="color: var(--color-heading); margin-bottom: var(--space-md);">Initiativbewerbung</h3>
            <p style="margin-bottom: var(--space-lg);">Wir verzichten auf starre Formulare. Ob Lebenslauf per Mail oder einfach ein kurzes Vorstellen – melde dich unverbindlich bei uns. Wir antworten rasch!</p>
            <a href="mailto:office@et-sl.at?subject=Initiativbewerbung" class="btn btn-primary btn-lg" style="width: 100%; max-width: 350px;">
              <i class="bi bi-envelope"></i>
              Bewerbung an office@et-sl.at
            </a>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt" style="background: var(--color-bg-alt); padding: var(--space-3xl) 0;">
      <div class="container">
        <div class="section-header" data-aos="fade-up">
          <h2>Was wir tun</h2>
          <p>Ein Einblick in unsere tägliche Arbeit.</p>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: var(--space-lg);" data-aos="fade-up" data-aos-delay="100">
          <a href="photovoltaik.html" class="service-card-mini" style="background: var(--color-white); padding: var(--space-xl); border-radius: var(--radius-lg); border: 1px solid var(--color-border); text-align: center; transition: all 0.3s ease;">
            <i class="bi bi-sun" style="font-size: 32px; color: var(--color-primary); margin-bottom: 15px; display: block;"></i>
            <h4 style="margin-bottom: 10px;">Photovoltaik</h4>
            <p style="font-size: var(--font-size-sm); color: var(--color-muted);">Installation von modernen Solaranlagen.</p>
          </a>
          <a href="elektroinstallation.html" class="service-card-mini" style="background: var(--color-white); padding: var(--space-xl); border-radius: var(--radius-lg); border: 1px solid var(--color-border); text-align: center; transition: all 0.3s ease;">
            <i class="bi bi-plug" style="font-size: 32px; color: var(--color-primary); margin-bottom: 15px; display: block;"></i>
            <h4 style="margin-bottom: 10px;">Elektroinstallation</h4>
            <p style="font-size: var(--font-size-sm); color: var(--color-muted);">Klassisches Handwerk und Smart Home.</p>
          </a>
        </div>
      </div>
    </section>
"""
    },
    "ueber-uns.html": {
        "title": "Über das Team | ET-SL Meisterbetrieb Elektrotechnik",
        "desc": "Lernen Sie die ET-SL GmbH kennen: Ihr Elektriker und Photovoltaik-Mesterbetrieb aus St. Radegund bei Graz. Regional, verlässlich, zertifiziert.",
        "keywords": "ET-SL Team, Elektriker St. Radegund, Meisterbetrieb Steiermark, Über uns",
        "content": """
    <section class="section" style="padding-top: var(--space-4xl);">
      <div class="container">
        <div class="section-header" data-aos="fade-up">
          <span class="section-label">Wir stellen uns vor</span>
          <h1>Über die ET-SL GmbH</h1>
        </div>
        
        <div style="max-width: 900px; margin: 0 auto; display: flex; flex-direction: column; gap: var(--space-xl);" data-aos="fade-up" data-aos-delay="100">
          
          <div style="border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-sm); aspect-ratio: 16/9; margin-bottom: var(--space-md);">
            <img src="assets/img/team/team.jpeg" alt="Das Team der ET-SL GmbH" style="width: 100%; height: 100%; object-fit: cover; object-position: center;">
          </div>
          
          <div style="line-height: 1.8; color: var(--color-muted);">
            <p style="font-size: var(--font-size-xl); margin-bottom: var(--space-lg); color: var(--color-heading); font-weight: 500;">
              Wir sind Ihr regionaler Meisterbetrieb für alle Belange der Elektrotechnik im Großraum Graz und Graz-Umgebung.
            </p>
            <p style="margin-bottom: var(--space-md);">
              Die ET-SL GmbH wurde mit dem klaren Anspruch gegründet, höchste handwerkliche Qualität mit modernsten und zukunftssicheren Technologien zu verbinden. Egal ob eine klassische Verkabelung, smarte Gebäudeautomation oder eine CO2-neutrale Photovoltaikanlage – unser Ansatz ist immer derselbe: Sicherheit, Zuverlässigkeit und eine restlos saubere Ausführung auf der Baustelle.
            </p>
            <p>
              Als tief in unserer Heimat <strong>St. Radegund</strong> verwurzeltes Unternehmen profitieren unsere Kunden von kurzen Wegen, schnellen Reaktionszeiten beim Störungsdienst und einem direkten, persönlichen Ansprechpartner ohne lange Warteschleifen. Kundenzufriedenheit ist für uns kein Marketing-Wort, sondern der Fixpunkt unserer täglichen Arbeit als Handwerker.
            </p>
          </div>
          
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: var(--space-lg); margin-top: var(--space-md);">
             <div style="background: var(--color-white); padding: var(--space-xl); border-radius: var(--radius-lg); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm); text-align: center;">
                 <i class="bi bi-shield-check" style="font-size: 36px; color: var(--color-primary); margin-bottom: 20px; display: inline-block;"></i>
                 <h4 style="color: var(--color-heading);">Geprüfter Meisterbetrieb</h4>
                 <p style="font-size: var(--font-size-sm); margin-top: 10px;">Fachgerechte Umsetzung nach höchsten sicherheitstechnischen ÖVE-Standards.</p>
             </div>
             <div style="background: var(--color-white); padding: var(--space-xl); border-radius: var(--radius-lg); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm); text-align: center;">
                 <i class="bi bi-map" style="font-size: 36px; color: var(--color-primary); margin-bottom: 20px; display: inline-block;"></i>
                 <h4 style="color: var(--color-heading);">Regional & Nah</h4>
                 <p style="font-size: var(--font-size-sm); margin-top: 10px;">Direkt aus St. Radegund betreuen wir private & gewerbliche Kunden im Raum Graz.</p>
             </div>
             <div style="background: var(--color-white); padding: var(--space-xl); border-radius: var(--radius-lg); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm); text-align: center;">
                 <i class="bi bi-plug" style="font-size: 36px; color: var(--color-primary); margin-bottom: 20px; display: inline-block;"></i>
                 <h4 style="color: var(--color-heading);">Lösungsorientiert</h4>
                 <p style="font-size: var(--font-size-sm); margin-top: 10px;">Vom kleinen Kurzschluss bis zum gewerblichen Großprojekt finden wir die beste Lösung.</p>
             </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt" style="background: var(--color-bg-alt); padding: var(--space-3xl) 0;">
      <div class="container">
        <div class="section-header" data-aos="fade-up">
          <h2>Unsere Kompetenzen</h2>
          <p>Erfahren Sie mehr über unsere Fachbereiche.</p>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: var(--space-lg);" data-aos="fade-up" data-aos-delay="100">
          <a href="photovoltaik.html" class="service-card-mini" style="background: var(--color-white); padding: var(--space-xl); border-radius: var(--radius-lg); border: 1px solid var(--color-border); text-align: center; transition: all 0.3s ease;">
            <i class="bi bi-sun" style="font-size: 32px; color: var(--color-primary); margin-bottom: 15px; display: block;"></i>
            <h4 style="margin-bottom: 10px;">Photovoltaik</h4>
            <p style="font-size: var(--font-size-sm); color: var(--color-muted);">Sonne nutzen – Strom sparen.</p>
          </a>
          <a href="elektroinstallation.html" class="service-card-mini" style="background: var(--color-white); padding: var(--space-xl); border-radius: var(--radius-lg); border: 1px solid var(--color-border); text-align: center; transition: all 0.3s ease;">
            <i class="bi bi-plug" style="font-size: 32px; color: var(--color-primary); margin-bottom: 15px; display: block;"></i>
            <h4 style="margin-bottom: 10px;">Elektroinstallation</h4>
            <p style="font-size: var(--font-size-sm); color: var(--color-muted);">Moderne Technik für Ihr Haus.</p>
          </a>
          <a href="e-mobilitaet.html" class="service-card-mini" style="background: var(--color-white); padding: var(--space-xl); border-radius: var(--radius-lg); border: 1px solid var(--color-border); text-align: center; transition: all 0.3s ease;">
            <i class="bi bi-ev-front" style="font-size: 32px; color: var(--color-primary); margin-bottom: 15px; display: block;"></i>
            <h4 style="margin-bottom: 10px;">E-Mobilität</h4>
            <p style="font-size: var(--font-size-sm); color: var(--color-muted);">Sicher laden zu Hause.</p>
          </a>
        </div>
      </div>
    </section>
"""
    }
}

for filename, data in pages.items():
    html_content = template_top.format(
        FILENAME=filename, 
        TITLE=data["title"], 
        DESC=data["desc"], 
        KEYWORDS=data["keywords"],
        BREADCRUMB=data.get("breadcrumb", data["title"].split("|")[0].strip())
    )
    html_content += data["content"]
    html_content += template_bottom
    
    with open(f"/home/ubuntu/Antigravity/ETSL/{filename}", "w") as f:
        f.write(html_content)

print("Generated 5 new HTML pages successfully.")
