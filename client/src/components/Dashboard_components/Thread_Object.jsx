import React from 'react';

function ThreadObject({
    id,
    thread_title,
    thread_content,
    category_id,
    likes
}){
    return(
       <div>
        <h1>{thread_title}</h1>
        <p>ID:{id}</p>
        <p>Content:{thread_content}</p>
        <p>Category ID:{category_id}</p>
        <i>❤️{likes}</i>
       </div>
    )
}


export default ThreadObject;