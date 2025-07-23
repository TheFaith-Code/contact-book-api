from fastapi import APIRouter, HTTPException
from typing import List
from .models import Contact

router = APIRouter()

# In-memory storage
contacts: List[Contact] = []

@router.post("/contacts", response_model=Contact)
def create_contact(contact: Contact):
    if any(c.id == contact.id for c in contacts):
        raise HTTPException(status_code=400, detail="Contact with this ID already exists")
    contacts.append(contact)
    return contact

@router.get("/contacts", response_model=List[Contact])
def get_contacts():
    return contacts

@router.get("/contacts/{contact_id}", response_model=Contact)
def get_contact(contact_id: int):
    for contact in contacts:
        if contact.id == contact_id:
            return contact
    raise HTTPException(status_code=404, detail="Contact not found")

@router.put("/contacts/{contact_id}", response_model=Contact)
def update_contact(contact_id: int, updated: Contact):
    for i, contact in enumerate(contacts):
        if contact.id == contact_id:
            contacts[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Contact not found")

@router.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int):
    for i, contact in enumerate(contacts):
        if contact.id == contact_id:
            contacts.pop(i)
            return {"message": "Contact deleted"}
    raise HTTPException(status_code=404, detail="Contact not found")