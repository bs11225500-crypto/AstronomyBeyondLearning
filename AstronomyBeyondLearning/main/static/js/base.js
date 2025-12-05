
function toggleMenu() {
    document.getElementById("mobileMenu").classList.toggle("show");
}


function dismissBanner() {
    const banner = document.getElementById("msgBanner");
    banner.classList.add("fade-out");

    setTimeout(() => {
        banner.style.display = "none";
    }, 350);
}


document.addEventListener("DOMContentLoaded", () => {
    document.body.classList.add("fade-in");
});


document.querySelectorAll("a[href]").forEach(link => {
    link.addEventListener("click", function (e) {
        const url = this.getAttribute("href");

        if (!url || url.startsWith("#") || this.target === "_blank") return;

        e.preventDefault();
        document.body.classList.add("fade-out");

        setTimeout(() => {
            window.location.href = url;
        }, 300);
    });
});


function revealOnScroll() {
    const items = document.querySelectorAll(".reveal");

    items.forEach(el => {
        const rect = el.getBoundingClientRect();
        const inView = rect.top < window.innerHeight - 80 && rect.bottom > 0;

        if (inView) {
            el.classList.add("active");
        } else {
            el.classList.remove("active");
        }
    });
}

window.addEventListener("scroll", revealOnScroll);
window.addEventListener("DOMContentLoaded", revealOnScroll);


document.addEventListener("DOMContentLoaded", () => {
    const items = document.querySelectorAll(".reveal");
    items.forEach((el, i) => {
        el.style.transitionDelay = (i * 0.07) + "s";
    });
});
