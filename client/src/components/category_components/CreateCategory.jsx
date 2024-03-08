import React, { useState } from 'react';
import { Formik, Form, useField } from 'formik';
import * as Yup from 'yup';

function CreateCategory(props){

    const [showCreateCategory, setShowCreateCategory] = useState(false);

    function handleClick(){
        setShowCreateCategory(!showCreateCategory);
    }
    
    const CategoryTextInput = ({ label, ...props }) => {
        const [field, meta] = useField(props);
        return (
            <div className="form-group">
                <label htmlFor={props.id || props.name}>{label}</label>
                <input className='text-input' {...field} {...props} />
                {meta.touched && meta.error ? (
                    <div className="error">{meta.error}</div>
                ) : null}
            </div>
        );
    }
    


        return (
        <div>
            {showCreateCategory ? (
            <Formik
                initialValues={{
                    category_name: '',
                    description: '',
                    user_id: '',
                }}
                validationSchema={Yup.object({
                    category_name: Yup.string()
                    .min(1, 'Name must be at least 1 characters long')
                    .required('Name is required'),
                    description: Yup.string()
                    .min(1, 'Description must be at least 1 characters long')
                    .required('Description is required'),
                })}
                onSubmit={(values, { setSubmitting, resetForm }) => {
                    fetch('http://localhost:5555/categories', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(values),
                })
                .then(res => res.json())
                .then(newCategory => {
                    props.onAddCategory(newCategory)
                    resetForm();
                    setSubmitting(false)
                })
          }}
        
            >
            <Form className='Create-Category-Form'>
                <CategoryTextInput label="Name" name="category_name" />
                <CategoryTextInput label="Description" name="description" />
                <button type="submit">Submit</button>
            </Form>

            </Formik>
            ) : null}
            <button className='Create-Category' onClick={handleClick}>{showCreateCategory ? "Cancel" : "Create A Category"}</button>
        </div>
            )
            
}

export default CreateCategory;