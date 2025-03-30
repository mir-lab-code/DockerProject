fetch('http://localhost:8000/images')
    .then(response => response.json())
    .then(data => {
        const imagesContainer = document.getElementById('images');
        data.images.forEach(image => {
            const imageElement = document.createElement('img');
            imageElement.src = image;
            imageElement.alt = image;
            imagesContainer.appendChild(imageElement);
        })
    });
//fetch('http://localhost/images')
//    .then(response => {response => response.json()})
//    .then(data => {
//        const imagesContainer = document.getElementByID('images');
//        data.images.forEach(image => {
//            const imageElement = document.createElement('img');
//            imageElement.src == '/images/${image}';
//            imageElement.alt = image;
//            imagesContainer.appendChild(imageElement);
//        })
//    })