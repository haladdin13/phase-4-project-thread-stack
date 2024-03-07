import React, { useState, useEffect } from 'react';

function PostObject({
    id,
    content,
    user_id,
    thread_id,
    likes,
    onSave,
    onDelete
}){

    const [editMode, setEditMode] = useState(false);
    const [editData, setEditData] = useState({
        content: content
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

    function handleDelete(){
        //set option for confirm deletion 
        const confirmDelete = window.confirm('Are you sure you want to delete?')

        if (confirmDelete){
            onDelete(id);
        }
    }

    if (editMode) {
        return (
            <div>
                <textarea
                name = "content"
                value = {editData.content}
                onChange = {handleChange}
                />
                <button onClick = {handleSave}>Save</button>
                <button onClick = {handleCancel}>Cancel</button>
            </div>
        )
    }


    return(
        <div>
            <p>{content}</p>
            <button onClick = {handleEdit}>Edit</button>
            <button onClick = {handleDelete}>Delete</button>
        </div>
    )
}

export default PostObject;