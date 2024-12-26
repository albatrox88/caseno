     // Mobile menu toggle functionality
     const menuToggle = document.querySelector('.menu-toggle');
     const navLinks = document.querySelector('.nav-links');

     menuToggle.addEventListener('click', () => {
         navLinks.classList.toggle('active');
         // Change icon based on menu state
         const icon = menuToggle.querySelector('i');
         if (navLinks.classList.contains('active')) {
             icon.classList.remove('fa-bars');
             icon.classList.add('fa-times');
         } else {
             icon.classList.remove('fa-times');
             icon.classList.add('fa-bars');
         }
     });

     // Close menu when clicking outside
     document.addEventListener('click', (e) => {
         if (!navLinks.contains(e.target) && !menuToggle.contains(e.target)) {
             navLinks.classList.remove('active');
             const icon = menuToggle.querySelector('i');
             icon.classList.remove('fa-times');
             icon.classList.add('fa-bars');
         }
     });

     // Close menu when clicking on a link
     navLinks.querySelectorAll('a').forEach(link => {
         link.addEventListener('click', () => {
             navLinks.classList.remove('active');
             const icon = menuToggle.querySelector('i');
             icon.classList.remove('fa-times');
             icon.classList.add('fa-bars');
         });
     });

     // Smooth scrolling for navigation links
     document.querySelectorAll('a[href^="#"]').forEach(anchor => {
         anchor.addEventListener('click', function (e) {
             e.preventDefault();
             document.querySelector(this.getAttribute('href'))?.scrollIntoView({
                 behavior: 'smooth'
             });
         });
     });

     // Add hover animations for platform cards
     document.querySelectorAll('.platform-card').forEach(card => {
         card.addEventListener('mouseenter', () => {
             card.style.transform = 'translateY(-5px)';
         });
         
         card.addEventListener('mouseleave', () => {
             card.style.transform = 'translateY(0)';
         });
     });

     // Add smooth scroll for all anchor links
     document.querySelectorAll('a[href^="#"]').forEach(anchor => {
         anchor.addEventListener('click', function (e) {
             e.preventDefault();
             document.querySelector(this.getAttribute('href'))?.scrollIntoView({
                 behavior: 'smooth'
             });
         });
     });

     // Add intersection observer for fade-in animations
     const observerOptions = {
         threshold: 0.1
     };

     const observer = new IntersectionObserver((entries) => {
         entries.forEach(entry => {
             if (entry.isIntersecting) {
                 entry.target.style.opacity = '1';
                 entry.target.style.transform = 'translateY(0)';
             }
         });
     }, observerOptions);

     document.querySelectorAll('.platform-card, .connect-item, .winners-gallery img').forEach(el => {
         el.style.opacity = '0';
         el.style.transform = 'translateY(20px)';
         el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
         observer.observe(el);
     });