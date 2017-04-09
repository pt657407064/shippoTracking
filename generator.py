import threading
from time import sleep

import shippo


class generator:
    shippo.api_key = "shippo_test_a0159d5cfb4013f15b4db6360f5be757edb6a2d4"

    def __init__(self,fromname,fromaddress,fromcity,fromstate,fromcountry,fromzipcode,fromemail,fromphone,
                      toname,toaddress,tocity,tostate,tocountry,tozipcode,toemail,tophone,
                      width,length,weight,unit,height):
        print(fromname,fromaddress,fromcity,fromstate,fromcountry,fromzipcode,fromemail,fromphone,
                      toname,toaddress,tocity,tostate,tocountry,tozipcode,toemail,tophone,
                      width,length,weight,unit,height)

        self.fromname = fromname
        self.fromaddress = fromaddress
        self.fromcity = fromcity
        self.fromstate = fromstate
        self.fromcountry = fromcountry
        self.fromzipcode = fromzipcode
        self.fromemail = fromemail
        self.fromphone = fromphone
        self.toname = toname
        self.toaddress = toaddress
        self.tocity = tocity
        self.tostate = tostate
        self.tocountry = tocountry
        self.tozipcode = tozipcode
        self.toemail = toemail
        self.tophone = tophone
        self.width = width
        self.length = length
        self.weight = weight
        if unit == "Inch":
            self.unit = "in"
        else:
            self.unit="cm"
        self.height = height



    def construct(self):
        self.person_from = {
            "name": self.fromname,
            "street1": self.fromaddress,
            "city": self.fromcity,
            "state": self.fromstate,
            "zip": self.fromzipcode,
            "country": self.fromcountry,
            "phone": self.fromphone,
            "email": self.fromemail
        }
        self.person_to = {
            "name": self.toname,
            "street1": self.toaddress,
            "city": self.tocity,
            "state": self.tostate,
            "zip": self.tozipcode,
            "country": self.tocountry,
            "phone": self.tophone,
            "email": self.toemail
        }
        self.parcel = {
            "length": self.length,
            "width": self.width,
            "height": self.height,
            "distance_unit": self.unit,
            "weight": self.weight,
            "mass_unit": "lb"
        }

    def generating(self):
        self.shipment = shippo.Shipment.create(
            address_from=self.person_from,
            address_to=self.person_to,
            parcels = self.parcel,
            async=False
        )

        print(self.person_to)
        print(self.person_from)
        print(self.parcel)
        rate = self.shipment.rates[0]
        transaction = shippo.Transaction.create(rate=rate.object_id, async=False)

        if transaction.status == "SUCCESS":
            print("tracking number %s" % str(transaction.tracking_number) + "\n" +
                  "Label url %s" % str(transaction.label_url))
        else:
            print("fail")

