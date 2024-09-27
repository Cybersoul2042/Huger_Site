document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("#image-add")?.addEventListener("click", () => AddImage());
    document.querySelector("#member-add")?.addEventListener("click", () => AddMember());
})

function AddImage(){
    console.log('panir')
    const images = document.querySelector(".images");

    if(images.children.length < 3){
        images.innerHTML += `<input autofocus class="form-control" type="file" name="image${images.children.length += 1}">`;
    }
}

function AddMember(){
    console.log('panir')
    const members = document.querySelector(".members");

    if(members.children.length < 3){
        members.innerHTML += `<div class="member-form">
                                <input autofocus class="form-control" type="text" placeholder="نام" name="member${members.children.length += 1}-name" required>
                                <input autofocus class="form-control" type="text" placeholder="نام خانوادگی" name="member${members.children.length += 1}-surname" required>
                                <input autofocus class="form-control" type="text" placeholder="تلفن همراه" name="member${members.children.length += 1}-number" required>
                                <div class="major-year">
                                    <select name="member${members.children.length += 1}-major" id="majors">
                                        <option value="ریاضی و فیزیک">ریاضی و فیزیک</option>
                                        <option value="تجربی">تجربی</option>
                                        <option value="انسانی">انسانی</option>
                                        <option value="شبکه و نرم افزار">شبکه و نرم افزار</option>
                                    </select>
                                    <select name="member${members.children.length += 1}-grade" id="years">
                                        <option value="دهم">دهم</option>
                                        <option value="یازدهم">یازدهم</option>
                                        <option value="دوازدهم">دوازدهم</option>
                                    </select>
                                </div>
                            </div>`;
    }
}

{/* */}