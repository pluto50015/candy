document.addEventListener("DOMContentLoaded", function () {
    const scroll = new LocomotiveScroll({
        el: document.querySelector("[data-scroll-container]"),
        smooth: true
    });

    const header = document.querySelector(".header");
    if (header) {
        scroll.on("scroll", () => {
            header.classList.toggle("scrolled", window.scrollY > 50);
        });
    } else {
        console.error("Error: `.header` が見つかりません");
    }
});
