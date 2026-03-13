// ===== IntersectionObserver for fade-in animations =====
document.addEventListener('DOMContentLoaded', function() {
    var observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -40px 0px'
    });

    document.querySelectorAll('.fade-in').forEach(function(el) {
        observer.observe(el);
    });

    // ===== FAQ toggle =====
    document.querySelectorAll('.faq-question').forEach(function(btn) {
        btn.addEventListener('click', function() {
            this.parentElement.classList.toggle('open');
        });
    });

    // ===== UTM parameter passthrough =====
    var params = new URLSearchParams(window.location.search);
    var utmKeys = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term'];
    var utmParams = {};

    utmKeys.forEach(function(key) {
        var val = params.get(key);
        if (val) {
            utmParams[key] = val;
        }
    });

    // If UTM params exist, append them to all LINE links
    if (Object.keys(utmParams).length > 0) {
        var utmString = new URLSearchParams(utmParams).toString();

        document.querySelectorAll('a[href*="lin.ee"], .btn-cta[data-line-url]').forEach(function(el) {
            var href = el.getAttribute('href') || el.getAttribute('data-line-url');
            if (href) {
                var separator = href.indexOf('?') !== -1 ? '&' : '?';
                var newHref = href + separator + utmString;
                if (el.tagName === 'A') {
                    el.setAttribute('href', newHref);
                }
                if (el.hasAttribute('data-line-url')) {
                    el.setAttribute('data-line-url', newHref);
                }
            }
        });

        // Handle onclick-based CTA buttons (hero CTA)
        document.querySelectorAll('.btn-cta[onclick]').forEach(function(el) {
            var onclick = el.getAttribute('onclick');
            if (onclick && onclick.indexOf('lin.ee') !== -1) {
                var match = onclick.match(/location\.href='([^']+)'/);
                if (match) {
                    var originalUrl = match[1];
                    var separator = originalUrl.indexOf('?') !== -1 ? '&' : '?';
                    var newUrl = originalUrl + separator + utmString;
                    el.setAttribute('onclick', "location.href='" + newUrl + "'");
                }
            }
        });
    }
});
