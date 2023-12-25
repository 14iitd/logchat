// Function to fetch posts from the API
async function fetchPosts() {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/feed/232');
    const data = await response.json();
    const postsContainer = document.getElementById('postsContainer');
    postsContainer.innerHTML = ''; // Clear previous posts

    data.posts.forEach(post => {
      const postElement = document.createElement('div');
      postElement.classList.add('post');
      postElement.innerHTML = `
        <p>${post.content}</p>
        <button onclick="likePost('${post._id}')">Like</button>
      `;
      postsContainer.appendChild(postElement);
    });
  } catch (error) {
    console.error('Error fetching posts:', error);
  }
}

// Function to create a new post
async function createPost() {
  try {
    const postContent = document.getElementById('postContent').value;
    const payload = {
      content: postContent
    };

    const response = await fetch('http://127.0.0.1:8000/api/posts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ZGVsaGl2ZXJ5cHVzaDpXUHdxTGxyc3E5Rjd4bnRxbzZqNG16TUYxVmQ3ZzVhag==',
        'user_id': '655a4205878d2d3c6b226771'
      },
      body: JSON.stringify(payload)
    });

    const newPost = await response.json();
    console.log('New post created:', newPost);

    // Fetch posts again to refresh the feed
    fetchPosts();
  } catch (error) {
    console.error('Error creating post:', error);
  }
}

// Function to like a post
async function likePost(postId) {
  try {
    // Implement the logic to like a post using the provided API
    // Send a request to like the post with postId
    console.log(`Liked post with ID: ${postId}`);
  } catch (error) {
    console.error('Error liking post:', error);
  }
}

// Fetch posts when the page loads
fetchPosts();
