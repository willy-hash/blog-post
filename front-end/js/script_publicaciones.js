document.addEventListener("DOMContentLoaded", () => {
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get("id");
    
    if (id) {
        fetch(`${id}`)
            .then(response => response.json())
            .then(data => {
                document.getElementById("titulo-noticia").textContent = data.titulo;
                document.getElementById("fecha-noticia").textContent = data.fecha;
                document.getElementById("imagen-noticia").src = data.imagen_url;
                document.getElementById("contenido-noticia").textContent = data.contenido;
            })
            .catch(error => console.error("Error cargando la noticia:", error));
    }

    // Cargar noticias populares
    fetch()
        .then(response => response.json())
        .then(noticias => {
            const contenedor = document.getElementById("noticias-populares");
            noticias.forEach(noticia => {
                const div = document.createElement("div");
                div.innerHTML = `
                    <h5>${noticia.titulo}</h5>
                    <p>${noticia.fecha}</p>
                `;
                contenedor.appendChild(div);
            });
        })
        .catch(error => console.error("Error cargando noticias populares:", error));

    // Cargar noticias relacionadas en el carrusel
    fetch()
        .then(response => response.json())
        .then(noticias => {
            const carouselContent = document.getElementById("carousel-content");
            noticias.forEach((noticia, index) => {
                const item = document.createElement("div");
                item.className = `carousel-item ${index === 0 ? 'active' : ''}`;
                item.innerHTML = `
                    <div class="card text-white">
                        <img src="${noticia.imagen_url}" class="card-img" alt="${noticia.titulo}">
                        <div class="card-img-overlay d-flex flex-column justify-content-end bg-dark bg-opacity-50">
                            <h5 class="card-title">${noticia.titulo}</h5>
                            <p>${noticia.fecha}</p>
                        </div>
                    </div>
                `;
                carouselContent.appendChild(item);
            });
        })
        .catch(error => console.error("Error cargando noticias relacionadas:", error));
    });