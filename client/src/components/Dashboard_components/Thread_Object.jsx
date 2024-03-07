import React, {useState, useEffect} from 'react';

function ThreadObject({
    id,
    thread_title,
    thread_content,
    category_id,
    likes,
    onSave
}){

    const [editMode, setEditMode] = useState(false);
    const [editData, setEditData] = useState({

        id: id,
        thread_title: thread_title,
        thread_content: thread_content,
        category_id: category_id,
        likes: likes
    })

    function handleEdit(){
        setEditMode(true);
    }

    function handleChange(e){
        const {name, value} = e.target
        setEditData(prev => ({
            ...prev,
            [name]: value
        }))
    }

    function handleSave(){
        onSave(id, editData);
        setEditMode(false);
    }

    function handleCancel(){
        setEditMode(false);
    }

    if (editMode) {
        return (
            <div>
                <input
                name = "thread_title"
                value = {editData.thread_title}
                onChange = {handleChange}
                />
                <textarea
                name = "thread_content"
                value = {editData.thread_content}
                onChange = {handleChange}
                />
                <button onClick = {handleSave}>Save</button>
                <button onClick = {handleCancel}>Cancel</button>
            </div>
        )
    }
    
    return(
       <div>
        <h1>{thread_title}</h1>
        <p>ID: {id}</p>
        <p>Content: {thread_content}</p>
        <p>Category ID: {category_id}</p>
        <i>❤️ {likes}</i>
        <button onClick = {handleEdit}>Edit</button>
       </div>
    )
}


export default ThreadObject;