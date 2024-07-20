def negamax(node, alpha, beta):
    if len(node.children) == 0:
        return node.value
    else:
        for child in node.children:
            val = -negamax(child, -beta, -alpha)
            if val >= beta:
                return val
            if val > alpha:
                alpha = val
        return alpha