import React from 'react';
import PostObject from './PostObject';

function PostContainer({renderPost, onSave, onDelete}){

    const postToRender = renderPost.map((postObj) => {
        return(
            <div key={postObj.id}>
                <PostObject {...postObj} onSave={onSave} onDelete={onDelete}/>
            </div>
        )
    })

    return(
        <div>
            <h1>Categories</h1>
            {postToRender}
        </div>
    )
}

export default PostContainer;