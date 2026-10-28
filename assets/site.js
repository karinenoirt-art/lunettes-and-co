// Lunettes & Co — menu, parcours de rendez-vous en 2 étapes, filtre des marques.
// Sans JavaScript, les boutons restent des liens vers la page Contact et rendez-vous.
(function () {
  var header = document.querySelector(".site-header");
  var toggle = document.querySelector(".menu-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = header.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  document.querySelectorAll(".nav-group > button").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      var group = btn.parentElement;
      var open = group.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });
  document.addEventListener("click", function () {
    document.querySelectorAll(".nav-group.open").forEach(function (g) {
      g.classList.remove("open");
      g.querySelector("button").setAttribute("aria-expanded", "false");
    });
  });

  // Parcours de rendez-vous : 1) type, 2) magasin
  var dialog = document.getElementById("rdv");
  if (dialog && typeof dialog.showModal === "function") {
    var steps = dialog.querySelectorAll("[data-step]");
    var chosenType = null;

    function show(step) {
      steps.forEach(function (s) { s.hidden = s.getAttribute("data-step") !== step; });
    }

    function fillStores(type) {
      chosenType = type;
      dialog.querySelectorAll("[data-type-notice]").forEach(function (n) {
        n.hidden = n.getAttribute("data-type-notice") !== type;
      });
      dialog.querySelectorAll("[data-store]").forEach(function (a) {
        var href = a.getAttribute("data-" + type);
        a.setAttribute("href", href);
        var external = /^https?:/.test(href);
        if (external) { a.setAttribute("target", "_blank"); a.setAttribute("rel", "noopener"); }
        else { a.removeAttribute("target"); a.removeAttribute("rel"); }
      });
      var title = dialog.querySelector("[data-step-title]");
      var labels = { tele: "Téléconsultation d'ophtalmologie", magasin: "Rendez-vous en magasin", libre: "Passer sans rendez-vous" };
      if (title) title.textContent = labels[type];
    }

    document.querySelectorAll("[data-open-rdv]").forEach(function (btn) {
      btn.addEventListener("click", function (e) {
        e.preventDefault();
        var type = btn.getAttribute("data-open-rdv");
        if (type) { fillStores(type); show("2"); } else { show("1"); }
        dialog.showModal();
      });
    });
    dialog.querySelectorAll("[data-choose]").forEach(function (btn) {
      btn.addEventListener("click", function () { fillStores(btn.getAttribute("data-choose")); show("2"); });
    });
    var back = dialog.querySelector(".rdv-back");
    if (back) back.addEventListener("click", function () { show("1"); });
    dialog.querySelector(".rdv-close").addEventListener("click", function () { dialog.close(); });
    dialog.addEventListener("click", function (e) { if (e.target === dialog) dialog.close(); });
  }

  // Filtre de la page Marques
  var filter = document.querySelector(".brand-filter");
  if (filter) {
    filter.addEventListener("click", function (e) {
      var btn = e.target.closest("button");
      if (!btn) return;
      filter.querySelectorAll("button").forEach(function (b) { b.setAttribute("aria-pressed", b === btn ? "true" : "false"); });
      var f = btn.getAttribute("data-filter");
      document.querySelectorAll(".brand").forEach(function (el) {
        var tags = el.getAttribute("data-tags");
        el.hidden = f !== "all" && tags.indexOf(f) === -1;
      });
    });
  }

  // Apparition douce des blocs au défilement (sans effet si l'utilisateur limite les animations)
  var calm = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if ("IntersectionObserver" in window && !calm) {
    var items = document.querySelectorAll("main section:not(.hero-full) .section-head, main .two-col > *, main .grid > *, main .faq, main .cta-band .wrap > *");
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    items.forEach(function (el, i) {
      el.classList.add("reveal");
      el.style.transitionDelay = (i % 3) * 90 + "ms";
      io.observe(el);
    });
    document.documentElement.classList.add("reveal-on");
  }

  // Cookies : Google Analytics n'est chargé qu'après accord. Le choix est gardé 6 mois, puis redemandé.
  var gaId = document.body.getAttribute("data-ga");
  var banner = document.getElementById("cookies");
  if (gaId && banner) {
    var KEY = "lc-consent";
    var SIX_MONTHS = 182 * 24 * 3600 * 1000;
    var THIRTEEN_MONTHS = 395 * 24 * 3600; // durée de vie maximale des cookies Analytics (CNIL)

    function readChoice() {
      try {
        var c = JSON.parse(localStorage.getItem(KEY));
        if (c && Date.now() - c.t < SIX_MONTHS) return c.v;
      } catch (e) {}
      return null;
    }
    function saveChoice(v) {
      try { localStorage.setItem(KEY, JSON.stringify({ v: v, t: Date.now() })); } catch (e) {}
    }
    function loadAnalytics() {
      if (window.gtag) return;
      window.dataLayer = window.dataLayer || [];
      window.gtag = function () { window.dataLayer.push(arguments); };
      window.gtag("js", new Date());
      window.gtag("config", gaId, { cookie_expires: THIRTEEN_MONTHS });
      var s = document.createElement("script");
      s.async = true;
      s.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(gaId);
      document.head.appendChild(s);
    }
    function removeAnalyticsCookies() {
      var host = location.hostname.replace(/^www\./, "");
      document.cookie.split(";").forEach(function (c) {
        var name = c.split("=")[0].trim();
        if (/^_ga/.test(name)) {
          ["", "; domain=" + host, "; domain=." + host].forEach(function (d) {
            document.cookie = name + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/" + d;
          });
        }
      });
    }
    function showBanner() { banner.hidden = false; }

    banner.addEventListener("click", function (e) {
      var btn = e.target.closest("[data-cookie]");
      if (!btn) return;
      var v = btn.getAttribute("data-cookie");
      saveChoice(v);
      banner.hidden = true;
      if (v === "accept") { loadAnalytics(); return; }
      window["ga-disable-" + gaId] = true; // coupe Analytics avant d'effacer ses cookies
      removeAnalyticsCookies();
      if (window.gtag) location.reload();
    });
    document.querySelectorAll("[data-cookie-settings]").forEach(function (el) {
      el.addEventListener("click", function (e) { e.preventDefault(); showBanner(); });
    });

    var choice = readChoice();
    if (choice === "accept") loadAnalytics();
    else {
      removeAnalyticsCookies(); // nettoie d'éventuels cookies laissés par un ancien accord
      if (choice === null) showBanner();
    }
  }
})();
