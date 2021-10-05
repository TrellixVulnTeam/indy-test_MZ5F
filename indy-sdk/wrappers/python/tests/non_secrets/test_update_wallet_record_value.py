import pytest

from indy import error
from tests.non_secrets.common import *


@pytest.mark.asyncio
async def test_update_wallet_record_value_works(wallet_handle):
    await non_secrets.add_wallet_record(wallet_handle, type_, id1, value1, tags_empty)
    await check_record_field(wallet_handle, "value", value1)

    await non_secrets.update_wallet_record_value(wallet_handle, type_, id1, value2)
    await check_record_field(wallet_handle, "value", value2)


@pytest.mark.asyncio
async def test_update_wallet_record_value_works_for_not_found_record(wallet_handle):
    with pytest.raises(error.WalletItemNotFound):
        await non_secrets.update_wallet_record_value(wallet_handle, type_, id1, value1)
