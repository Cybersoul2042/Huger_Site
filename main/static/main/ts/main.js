document.addEventListener("DOMContentLoaded", function () {
    var _a, _b;
    (_a = document.querySelector("#project")) === null || _a === void 0 ? void 0 : _a.addEventListener("click", function () { return ChangePage("project"); });
    (_b = document.querySelector("#submit")) === null || _b === void 0 ? void 0 : _b.addEventListener("click", function () { return ChangePage("submit"); });
    ChangePage('home');
});
function ChangePage(page) {
    var _a;
    var bodyPages = (_a = document.querySelector('.body-container')) === null || _a === void 0 ? void 0 : _a.children;
    // @ts-ignore
    for (var _i = 0, _b = bodyPages; _i < _b.length; _i++) {
        var child = _b[_i];
        if ((child.className) == "".concat(page, "-page")) {
            child.style.display = "block";
        }
        else {
            child.style.display = "none";
        }
    }
}
//# sourceMappingURL=main.js.map