document.addEventListener("DOMContentLoaded", () => {
    const paisSelect = document.getElementById("pais");
    fetch("https://restcountries.com/v3.1/all")
        .then(response => response.json())
        .then(data => {
            paisSelect.innerHTML = '<option value="">Seleccione su país</option>';
            data.sort((a, b) => a.name.common.localeCompare(b.name.common));
            data.forEach(pais => {
                const option = document.createElement("option");
                option.value = pais.name.common;
                option.textContent = pais.name.common;
                paisSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error("Error cargando países:", error);
            paisSelect.innerHTML = '<option value="">Error cargando países</option>';
        });

    document.getElementById("registro-form").addEventListener("submit", (event) => {
        event.preventDefault();
        const usuario = {
            nombre: document.getElementById("nombre").value,
            email: document.getElementById("email").value,
            password: document.getElementById("password").value,
            fechaNacimiento: document.getElementById("fechaNacimiento").value,
            pais: document.getElementById("pais").value
        };
        
        fetch("http://localhost:8080/registrar", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(usuario)
        })
        .then(response => response.json())
        .then(data => {
            alert("Registro exitoso");
            window.location.href = "verPerfil.html";
        })
        .catch(error => console.error("Error en el registro:", error));
    });
});