fetch('http://localhost:8000/images')
    .then(response => response.json())
    .then(data => {
        const imagesContainer = document.getElementById('images');
        data.images.forEach(image => {
            const a = document.createElement('a');
            a.href = '/images/' + image;
            imagesContainer.appendChild(a);

            const imageElement = document.createElement('img');
            imageElement.src = image;
            imageElement.alt = image;

            a.appendChild(imageElement);
        })
    });