import React, {useState, useEffect} from "react";
import CategoryContainer from "./category_components/CategoryContainer";
import CreateCategory from "./category_components/CreateCategory";


function Category(){

    const [renderCategory, setRenderCategory] = useState([]);

    const addCategory = (newCategory) => {
        console.log(newCategory); 
        if (newCategory && newCategory.id) {
            setRenderCategory(prevCategories => [...prevCategories, newCategory]);
        } else {
            console.error('Attempted to add an undefined or invalid category:', newCategory);
        }
    };
    

    useEffect(() =>{
        fetch(`http://localhost:5555/categories`).then(res => {
            if (res.status != 200){
                console.log("error")
                return
            }
            res.json().then(data => {
                if (data != null){
                    setRenderCategory(data)
                    console.log(data)
                }
            })
        })
    }, []);

    function handleSaveCategory(id, updatedCategory){
        fetch(`http://localhost:5555/categories/${id}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updatedCategory),
        })
     .then(res => res.json())
     .then(data => {

        setRenderCategory(prevCategories => prevCategories.map(category => 
            category.id === data.id ? data : category
        ));
    })
    }

    function handleDeleteCategory(id) {
        fetch(`http://localhost:5555/categories/${id}`, {
            method: 'DELETE',
        })
        .then(response => {
                setRenderCategory(prevCategories => 
                    prevCategories.filter(category => category.id !== id)
                );
        })
    }
    

    return(
        <div>
            <CreateCategory onAddCategory={addCategory} />
            <CategoryContainer renderCategory={renderCategory} onSave={handleSaveCategory} onDelete={handleDeleteCategory}/>
        </div>
    )
}

export default Category;