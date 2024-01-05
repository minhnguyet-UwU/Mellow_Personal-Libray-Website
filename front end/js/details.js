$(document).ready(function () {
    $(".like-icon").click(function () {
        document.addEventListener("DOMContentLoaded", function () {
             toggleLike();
            });const likeButton = document.querySelector('.like-button');
            
            likeButton.addEventListener('click', function () {
               
        });
        
        let isLiked = false;
        let likeCount = 1537;
        
        function toggleLike() {
            if (isLiked) {
                // If already liked, unlike
                likeCount--;
                isLiked = false;
            } else {
                // If not liked, like
                likeCount++;
                isLiked = true;
            }
        
            // Update like count and icon color
            document.getElementById('like-count').textContent = likeCount;
            updateLikeIcon();
        }
        
        function updateLikeIcon() {
            const likeIcon = document.querySelector('.like-icon');
        
            // Toggle between filled and outlined heart icons
            if (isLiked) {
                likeIcon.classList.remove('fa-thumbs-o-up');
                likeIcon.classList.add('fa-thumbs-up');
            } else {
                likeIcon.classList.remove('fa-thumbs-up');
                likeIcon.classList.add('fa-thumbs-o-up');
            }
        }
        
    });

});

