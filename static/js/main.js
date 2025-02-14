document.addEventListener("DOMContentLoaded", function () {
    const header = document.getElementById("header");
    const scrollContainer = document.querySelector("[data-scroll-container]");

    const scroll = new LocomotiveScroll({
        el: scrollContainer,
        smooth: true
    });

    scroll.on("scroll", (instance) => {
        if (instance.scroll.y > 100) {
            header.classList.add("fixed");
            scrollContainer.style.transform = "none";  // 🔹 transform を無効化
        } else {
            header.classList.remove("fixed");
            scrollContainer.style.transform = "";  // 🔹 元に戻す
        }
    });
});
