const express = require('express');
const Stripe = require('stripe');
const app = express();
const stripe = Stripe('sk_test_YOUR_SECRET_KEY');

app.use(express.json());

app.post('/create-payment-intent', async (req, res) => {
  const paymentIntent = await stripe.paymentIntents.create({
    amount: 1000, // £10.00
    currency: 'gbp',
  });

  res.send({
    clientSecret: paymentIntent.client_secret,
  });
});

app.listen(3000, () => console.log('Server running on port 3000'));
