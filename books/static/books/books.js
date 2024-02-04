const form = document.querySelector("#search-form");
const resetBtn = document.querySelector("#btn-reset");

resetBtn.addEventListener("click", function(){
    console.log(form)
    form.reset();
})