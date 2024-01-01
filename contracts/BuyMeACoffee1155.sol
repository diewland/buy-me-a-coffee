// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import "@openzeppelin/contracts/token/ERC1155/presets/ERC1155PresetMinterPauser.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract BuyMeACoffee1155 is ERC1155PresetMinterPauser {

    string public name = "Buy Me A Coffee";
    string public symbol = "COFFEE";
    string private baseURI = "ipfs://bafybeiamz6sbqyerpkioritvhekvb4h2nicq3ldzyuvdjroj5hs7gqzbb4/";

    constructor() ERC1155PresetMinterPauser("") {
        _mint(msg.sender, 1, 99, "");  // Daily
        _mint(msg.sender, 2, 99, "");  // Weekly
        _mint(msg.sender, 3, 99, "");  // Monthly
        _mint(msg.sender, 4, 99, "");  // Yearly
    }

    // mint
    function adminMint(uint256 id, uint256 amount) public virtual {
        require(hasRole(DEFAULT_ADMIN_ROLE, _msgSender()), "admin only");
        mint(_msgSender(), id, amount, "");
    }

    // metadata
    function setBaseURI(string calldata _newBaseURI) external {
        require(hasRole(DEFAULT_ADMIN_ROLE, _msgSender()), "admin only");
        baseURI = _newBaseURI;
    }
    function tokenURI(uint tokenId) public view returns (string memory) {
        return string.concat(baseURI, Strings.toString(tokenId), ".json");
    }

}
