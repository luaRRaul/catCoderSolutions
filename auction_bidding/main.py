def main():
    info = []
    info.append('-')
    highestBidder=''
    highestBid=1
    inn = input().split(',')
    price=int(inn[0])
    for i in range(1,len(inn)-1,2):
        priceBeforeEachBid = price
        name, bid = inn[i:i+2]
        bid = int(bid)
        if bid > price:
            if highestBidder == '':
                highestBidder=name
                highestBid=bid
                info.append([highestBidder, price])
            else:
                if bid > highestBid:
                    if highestBidder != name:
                        price=highestBid+1
                        highestBidder=name
                        highestBid=bid
                    else:
                        highestBid=bid
                        highestBidder=name
                else:
                    if highestBidder != name:
                        price=bid+1
        else:
            if highestBidder !='':
                price=bid+1

        if priceBeforeEachBid != price or highestBidder != name:
            info.append([highestBidder, price])
    if len(inn) == 3:
        highestBidder=inn[1]
    # print(f'{highestBidder},{price}')
    print(info[0], end=',')
    for name,price in info[1:]:
        print(f'{name},{price}', end=',');





if __name__ == "__main__":
    main()
