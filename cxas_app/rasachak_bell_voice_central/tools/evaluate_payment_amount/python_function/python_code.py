def evaluate_payment_amount(payment_amount: float, pastDueAmount: float, currentBalance: float) -> dict:
    '''State Manipulator Tool to handle float comparisons for payment amounts safely outside the LLM.'''
    try:
        amt = float(payment_amount) if payment_amount else 0.0
        past_due = float(pastDueAmount) if pastDueAmount else 0.0
        curr_bal = float(currentBalance) if currentBalance else 0.0

        print("Business logic success - Evaluated payment amount")
        if amt < past_due:
            return {"status": "TOO_LOW", "amount": amt, "pastDueAmount": past_due}
        elif amt > curr_bal:
            return {"status": "EXCEEDS_BALANCE", "amount": amt, "currentBalance": curr_bal}
        else:
            return {"status": "VALID_AMOUNT", "amount": amt}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the user that there was an error verifying the amount and ask them to repeat it."}