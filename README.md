# acme-shopping-cart


## Overview  
This is a Python-based shopping cart system for Acme Widget Co, implementing product pricing, discount rules, and delivery charges.

## Features  
- **Product Catalog**: Supports Red, Green, and Blue widgets.  
- **Promotions**: "Buy One Red Widget (R01), Get Second at Half Price" applied automatically.  
- **Delivery Charges**:  
  - Orders **under $50** → $4.95 shipping  
  - Orders **under $90** → $2.95 shipping  
  - Orders **$90+** → Free shipping
- **Additional Features**:  
  - **Remove items** from the cart.  
  - **View cart contents** before checkout.
 
## Assumptions  
- The **"Buy One R01, Get Second at Half Price"** applies only to **R01** in pairs.  
- Delivery charge is **calculated after discounts**.  
- Users can **add, remove, and view cart items** before checkout.  
