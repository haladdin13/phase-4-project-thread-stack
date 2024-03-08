import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function CategoryObject({
    id,
    category_name,
    description,
    user_id,
    threads,
    onSave,
    onDelete
}){

    const [editMode, setEditMode] = useState(false);
    const [editData, setEditData] = useState({
        id: id,
        category_name: category_name,
        description: description,
        user_id: user_id,
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
            <div className="EditCategoryForm">
                <input
                name = "category_name"
                value = {editData.category_name}
                onChange = {handleChange}
                />
                <textarea
                name = "description"
                value = {editData.description}
                onChange = {handleChange}
                />
                <button onClick = {handleSave}>Save</button>
                <button onClick = {handleCancel}>Cancel</button>
            </div>
        )
    }


    return(
        <div className='CategoryObject'>
            <Link to={`/categories/${id}`}>
            <h1>{category_name}</h1>
            </Link>
            <p>ID: {id}</p>
            <p>Description: {description}</p>
            <p>User ID: {user_id}</p>
            <button onClick = {handleEdit}>Edit</button>
            <button onClick = {handleDelete}>Delete</button>
        </div>
    )
}

export default CategoryObject;