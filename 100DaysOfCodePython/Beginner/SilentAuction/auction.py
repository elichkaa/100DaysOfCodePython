import art
import messages


def find_winner(bidders):
    top = 0
    winner = ""
    for bidder in bidders:
        if bids[bidder] > top:
            top = bids[bidder]
            winner = bidder
    return winner, top


if __name__ == '__main__':
    print(art.logo)
    print(messages.welcome)
    other = True
    bids = {}
    while other:
        name = input(messages.name)
        bid = input(messages.bid)
        bids[name] = float(bid)
        other = input(messages.other)
        if other == messages.stop:
            other = False
            win, t = find_winner(bids)
            print(messages.winner(win, t))
