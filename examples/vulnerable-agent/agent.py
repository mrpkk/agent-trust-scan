"""Intentionally unsafe demo agent. Fake key, fake wallet, no controls."""

from config import PRIVATE_KEY


def pay(tx, token, spender, tool_output):
    # x402-style payment path with no receipt check
    token.approve(spender, type(uint256).max)
    wallet.send_transaction(tx)
    return eval(tool_output)


def main(tx, token, spender, tool_output):
    return pay(tx, token, spender, tool_output)
