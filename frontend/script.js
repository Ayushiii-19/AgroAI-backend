async function predict(){
    let file = document.getElementById("img").files[0];
    let form = new FormData();
    form.append("image", file);

    let res = await fetch("http://127.0.0.1:5000/predict", { method:"POST", body:form });
    let data = await res.json();

    document.getElementById("output").innerText =
        `Disease: ${data.Disease} | Accuracy: ${data.Accuracy}% | Treatment: ${data.Treatment}`;
}
