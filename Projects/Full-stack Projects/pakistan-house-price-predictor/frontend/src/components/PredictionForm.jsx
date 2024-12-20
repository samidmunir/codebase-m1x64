import React, { useState } from "react";
import FormInput from "./FormInput";
import { predict } from "../services/api";

const PredictionForm = () => {
    const [formData, setFormData] = useState({
        bedrooms: "",
        baths: "",
        size: "",
        bed_bath_ratio: "",
        price_per_sqft: "",
        total_rooms: "",
        luxury_index: "",
        FECHS_2: 0,
        Attock: 0,
        Faisalabad: 0,
        Gujranwala: 0,
        Islamabad: 0,
        Karachi: 0,
        Lahore: 0,
        Multan: 0,
        Murree: 0,
        Peshawar: 0,
        Quetta: 0,
        Rawalpindi: 0,
    });

    const [prediction, setPrediction] = useState(null);

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setFormData({
            ...formData,
            [name]: type === "checkbox" ? (checked ? 1 : 0) : value,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const result = await predict(formData);
            setPrediction(result);
        } catch (error) {
            alert("Error making prediction.");
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <FormInput label="Bedrooms" name="bedrooms" type="number" value={formData.bedrooms} onChange={handleChange} />
            <FormInput label="Baths" name="baths" type="number" value={formData.baths} onChange={handleChange} />
            <FormInput label="Size" name="size" type="number" value={formData.size} onChange={handleChange} />
            <FormInput label="Bed Bath Ratio" name="bed_bath_ratio" type="number" value={formData.bed_bath_ratio} onChange={handleChange} />
            <FormInput label="Price per Sqft" name="price_per_sqft" type="number" value={formData.price_per_sqft} onChange={handleChange} />
            <FormInput label="Total Rooms" name="total_rooms" type="number" value={formData.total_rooms} onChange={handleChange} />
            <FormInput label="Luxury Index" name="luxury_index" type="number" value={formData.luxury_index} onChange={handleChange} />

            <h4>City</h4>
            {["FECHS_2", "Attock", "Faisalabad", "Gujranwala", "Islamabad", "Karachi", "Lahore", "Multan", "Murree", "Peshawar", "Quetta", "Rawalpindi"].map((city) => (
                <label key={city}>
                    <input type="checkbox" name={city} checked={!!formData[city]} onChange={handleChange} />
                    {city}
                </label>
            ))}
            <button type="submit">Predict</button>
            {prediction && <h3>Prediction: {prediction}</h3>}
        </form>
    );
};

export default PredictionForm;
