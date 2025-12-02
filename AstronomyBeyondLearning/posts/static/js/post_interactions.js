document.addEventListener('DOMContentLoaded', () => {

    async function toggleLike(postId, likeButton) {

        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; 
        
        const url = `/post/${postId}/like/`;

        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken, 
                    'Content-Type': 'application/json'
                },
            });

            if (!response.ok) {
                throw new Error(`Server responded with status: ${response.status}`);
            }

            const data = await response.json(); 

            const likeCountElement = likeButton.querySelector('.like-count');

            if (data.is_liked) {

                likeButton.classList.add('liked');
            } else {

                likeButton.classList.remove('liked');
            }
            
            likeCountElement.textContent = formatCount(data.total_likes);

        } catch (error) {
            console.error('Error toggling like:', error);
            alert("Could not process the request. Please log in or try again later.");
        }
    }

    function formatCount(num) {
        if (num >= 1000) {
            return (num / 1000).toFixed(1) + 'K';
        }
        return num.toString();
    }
    document.body.addEventListener('click', (e) => {
        const likeButton = e.target.closest('.like-btn'); 

        if (likeButton) {
            const postId = likeButton.dataset.postId; 
            
            if (postId) {
                toggleLike(postId, likeButton);
            }
        }
    });

});


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookies[i].substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


//  منطق حذف البوست (Post Deletion Logic)
document.addEventListener('DOMContentLoaded', function() {
    const deleteForm = document.getElementById('delete-post-form');

    if (deleteForm) {
        deleteForm.addEventListener('submit', function(e) {
            e.preventDefault(); 

            const confirmed = confirm("Are you sure you want to delete this post? This action cannot be undone.");
            
            if (confirmed) {
                const url = deleteForm.getAttribute('action');
                
                fetch(url, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': csrftoken,
                        'Content-Type': 'application/json'
                    },
                })
                .then(response => {
                    if (response.status === 200) {
                        return response.json();
                    } else if (response.status === 403) {
                        alert("Error: You do not have permission to delete this post.");
                        return Promise.reject('Forbidden');
                    } else {
                        alert("An error occurred while deleting the post.");
                        return Promise.reject('Error');
                    }
                })
                .then(data => {
                    if (data.success) {
                        alert(data.message);
                        window.location.href = "/"; 
                    }
                })
                .catch(error => {
                    console.error('Fetch error:', error);
                });
            }
        });
    }

    //  منطق حذف التعليقات (Comment Deletion Logic)
    document.querySelectorAll('.delete-comment-btn').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const commentId = this.dataset.commentId; 
            const deleteUrl = `/comment/${commentId}/delete/`;
            const commentElement = this.closest('.comment-item'); 

            const confirmed = confirm("Are you sure you want to delete this comment?");
            
            if (confirmed) {
                fetch(deleteUrl, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': csrftoken,
                        'Content-Type': 'application/json'
                    },
                })
                .then(response => {
                    if (response.status === 200) {
                        return response.json();
                    } else if (response.status === 403) {
                        alert("Error: You do not have permission to delete this comment.");
                        return Promise.reject('Forbidden');
                    } else {
                        alert("An error occurred while deleting the comment.");
                        return Promise.reject('Error');
                    }
                })
                .then(data => {
                    if (data.success) {
                        commentElement.remove();
                    }
                })
                .catch(error => {
                    console.error('Fetch error:', error);
                });
            }
        });
    });


    //  منطق الإشارة المرجعية (Bookmark Toggle Logic)
    document.querySelectorAll('.bookmark-toggle').forEach(button => {
        button.addEventListener('click', function() {
            const postId = this.dataset.postId;
            const url = `/post/${postId}/bookmark/`; 

            fetch(url, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken,
                    'Content-Type': 'application/json'
                }
            })
            .then(response => {
                if (!response.ok) {
                    alert("Please log in to save this post.");
                    return Promise.reject('Not authenticated');
                }
                return response.json();
            })
            .then(data => {
                if (data.is_bookmarked) {
                    this.textContent = 'Unsave'; 
                    this.classList.add('bookmarked'); 
                    this.classList.remove('not-bookmarked');
                } else {
                    this.textContent = 'Save'; 
                    this.classList.add('not-bookmarked');
                    this.classList.remove('bookmarked');
                }
                console.log(data.message);
            })
            .catch(error => {
                console.error('Bookmark error:', error);
            });
        });
    });

});