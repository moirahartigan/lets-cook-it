// js for message to dismiss itself
setTimeout(function() {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
},3000);

// owl-carousel jquery
// https://htmlcss3tutorials.com/owl-carousel-slider-bootstrap-5-example/
$('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:2
        },
        1000:{
            items:4
        }
    }
})


