import pandas as pd
import numpy as np
from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import logging

logger = logging.getLogger(__name__)

class PropertyAnalyzer:
    def __init__(self):
        try:
            # Initialize BERT model and tokenizer
            self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
            self.model = BertModel.from_pretrained('bert-base-uncased')
            self.model.eval()  # Set to evaluation mode
            logger.info("Successfully loaded BERT model")
        except Exception as e:
            logger.error(f"Failed to load BERT model: {str(e)}")
            self.model = None
            self.tokenizer = None
        
    def get_bert_embeddings(self, texts):
        """Get BERT embeddings for a list of texts."""
        if self.model is None or self.tokenizer is None:
            return None
            
        try:
            # Tokenize and prepare inputs
            inputs = self.tokenizer(texts, padding=True, truncation=True, return_tensors="pt", max_length=512)
            
            # Get embeddings
            with torch.no_grad():
                outputs = self.model(**inputs)
                # Use the [CLS] token embedding (first token) as the sentence embedding
                embeddings = outputs.last_hidden_state[:, 0, :].numpy()
            
            return embeddings
        except Exception as e:
            logger.error(f"Error getting BERT embeddings: {str(e)}")
            return None
    
    def generate_summary(self, df):
        """Generate a summary of the property market analysis."""
        try:
            # Calculate key statistics
            avg_price = df['Price'].mean()
            median_price = df['Price'].median()
            price_range = (df['Price'].min(), df['Price'].max())
            top_locations = df['Location'].value_counts().head(3)
            avg_marla = df['Marla'].mean()
            avg_bedrooms = df['Bedrooms'].mean()
            
            # Create summary points
            summary_points = [
                f"The average property price is Rs. {avg_price:,.0f}",
                f"The median property price is Rs. {median_price:,.0f}",
                f"Prices range from Rs. {price_range[0]:,.0f} to Rs. {price_range[1]:,.0f}",
                f"Top locations are {', '.join(top_locations.index)}",
                f"Average property size is {avg_marla:.1f} Marla",
                f"Average number of bedrooms is {avg_bedrooms:.1f}"
            ]
            
            # Get BERT embeddings
            embeddings = self.get_bert_embeddings(summary_points)
            
            if embeddings is not None:
                # Find most representative points using cosine similarity
                avg_embedding = np.mean(embeddings, axis=0)
                similarities = cosine_similarity([avg_embedding], embeddings)[0]
                top_indices = np.argsort(similarities)[-3:][::-1]
                
                # Generate final summary
                summary = "Market Analysis Summary:\n\n"
                for idx in top_indices:
                    summary += f"- {summary_points[idx]}\n"
            else:
                # Fallback to basic summary if model is not available
                summary = "Market Analysis Summary:\n\n"
                for point in summary_points[:3]:  # Take first 3 points
                    summary += f"- {point}\n"
            
            return summary
        except Exception as e:
            logger.error(f"Error generating summary: {str(e)}")
            return "Error generating market summary. Please try again later."
    
    def generate_predictions(self, df):
        """Generate market predictions based on the data."""
        try:
            # Calculate trends
            price_trend = df.groupby('Location')['Price'].mean().sort_values(ascending=False)
            location_growth = df['Location'].value_counts().pct_change().mean()
            
            # Create prediction points
            prediction_points = [
                f"Top locations by price are {', '.join(price_trend.head(3).index)}",
                f"Market size is {len(df):,} properties",
                f"Average location growth rate is {location_growth:.2%}",
                f"Premium locations show strong price performance",
                f"Consider investing in high-growth areas"
            ]
            
            # Get BERT embeddings
            embeddings = self.get_bert_embeddings(prediction_points)
            
            if embeddings is not None:
                # Find most representative points
                avg_embedding = np.mean(embeddings, axis=0)
                similarities = cosine_similarity([avg_embedding], embeddings)[0]
                top_indices = np.argsort(similarities)[-3:][::-1]
                
                # Generate final predictions
                predictions = "Market Predictions:\n\n"
                for idx in top_indices:
                    predictions += f"- {prediction_points[idx]}\n"
            else:
                # Fallback to basic predictions if model is not available
                predictions = "Market Predictions:\n\n"
                for point in prediction_points[:3]:  # Take first 3 points
                    predictions += f"- {point}\n"
            
            return predictions
        except Exception as e:
            logger.error(f"Error generating predictions: {str(e)}")
            return "Error generating market predictions. Please try again later."

def get_market_insights(df):
    """Get market insights including summary and predictions."""
    try:
        analyzer = PropertyAnalyzer()
        summary = analyzer.generate_summary(df)
        predictions = analyzer.generate_predictions(df)
        
        return {
            "summary": summary,
            "predictions": predictions
        }
    except Exception as e:
        logger.error(f"Error in get_market_insights: {str(e)}")
        # Fallback to basic statistical summary if model fails
        avg_price = df['Price'].mean()
        top_locations = df['Location'].value_counts().head(3)
        
        return {
            "summary": f"Market Summary:\n- Average property price: Rs. {avg_price:,.0f}\n- Top locations: {', '.join(top_locations.index)}",
            "predictions": "Market predictions currently unavailable. Please try again later."
        } 