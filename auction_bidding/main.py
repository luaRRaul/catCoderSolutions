def main():
    info = []
    info.append('-')
    highestBidder=''
    highestBid=1
    inn = input().split(',')
    price=int(inn[0])
    buyNowPrice=int(inn[1])
    info.append(price);
    for i in range(2,len(inn)-1,2):
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
                    if bid == highestBid:
                            price=bid
                    else:
                        if highestBidder != name:
                            price=bid+1
        else:
            if highestBidder !='':
                price=bid+1
            else:
                highestBidder=name
                info.append([highestBidder, price])

        if price >= buyNowPrice and buyNowPrice !=0:
            info.append([highestBidder, buyNowPrice])
            break;

        if priceBeforeEachBid != price or highestBidder != name:
            info.append([highestBidder, price])
    if len(inn) == 3:
        highestBidder=inn[1]
    # print(f'{highestBidder},{price}')
    print(info[0], end=',')
    print(info[1], end=',')
    for name,price in info[2:]:
        print(f'{name},{price}', end=',');





if __name__ == "__main__":
    main()
